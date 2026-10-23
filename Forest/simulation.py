import random
from config import EMPTY, TREE, FIRE, WATER,  BASE_GROWTH_PROBABILITY, GROWTH_PROBABILITY, LIGHTNING_PROBABILITY, WATER_GROWTH_PROBABILITY_1, WATER_GROWTH_PROBABILITY_2

#----------------------------------------------------------------------------------------------------#

def generate_forest(rows,columns,tree_probability):
    forest = [] 
    for i in range(rows):
        new_row = []
        for j in range(columns):
            fate = random.random()

            if fate < tree_probability:
                new_row.append(TREE)
            else:
                new_row.append(EMPTY)

        forest.append(new_row)
    return forest

#----------------------------------------------------------------------------------------------------#

def add_river(forest):
    cols = len(forest[0])
    c = random.randint(0,cols-1)
    for r in range(len(forest)):
        if c < 0 or c >= cols:
            break
        forest[r][c] = WATER
        c += random.choice([-1, 0, 1])

#----------------------------------------------------------------------------------------------------#

def has_neighbor(forest, row_idx, col_idx, target):
    for r in range(row_idx-1,row_idx+2):
        for c in range(col_idx-1,col_idx+2):
            if r == row_idx and c == col_idx:
                continue
            if 0<= r < len(forest) and 0 <= c < len(forest[0]):
                if forest[r][c] == target:
                    return True
    return False

#----------------------------------------------------------------------------------------------------#

def update_forest(forest):
    new_forest = []
    for r in range(len(forest)):
        new_row = []
        for c in range(len(forest[0])):
            if forest[r][c] == TREE and (has_neighbor(forest, r, c, FIRE) or random.random() < LIGHTNING_PROBABILITY):
                new_row.append(FIRE)
            elif forest[r][c] == FIRE:
                new_row.append(EMPTY)
            elif forest[r][c] == EMPTY:
                fate = random.random()
                if has_neighbor(forest, r, c, TREE) and has_neighbor(forest, r, c, WATER):
                    chance = WATER_GROWTH_PROBABILITY_1
                elif has_neighbor(forest, r, c, WATER):
                    chance = WATER_GROWTH_PROBABILITY_2
                elif has_neighbor(forest, r, c, TREE):
                    chance = GROWTH_PROBABILITY
                else:
                    chance = BASE_GROWTH_PROBABILITY
                if fate < chance:
                    new_row.append(TREE)
                else:
                    new_row.append(EMPTY)
            else:
                new_row.append(forest[r][c])
        new_forest.append(new_row)
    return new_forest

#----------------------------------------------------------------------------------------------------#

def is_fire_burning(forest):
    for row in forest:
        if FIRE in row:
            return True
    return False

#----------------------------------------------------------------------------------------------------#

def count_cells(forest, target):
    total = 0
    for row in forest:
        total += row.count(target)
    return total