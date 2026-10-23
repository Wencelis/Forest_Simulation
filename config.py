EMPTY = 0
TREE = 1
FIRE = 2


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