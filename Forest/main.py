import time
import random
from rich.console import Console

from config import TREE, FIRE, SLEEP_TIME, ROWS, COLUMNS, TREE_PROBABILITY
from simulation import is_fire_burning, update_forest, count_cells, generate_forest, add_river
from visualizer import create_dashboard

#----------------------------------------------------------------------------------------------------#


def main():
    first = generate_forest(ROWS, COLUMNS, TREE_PROBABILITY)
    max_fire = 0
    max_tree = 0
    total_tree = 0
    total_fire = 0
    step = 1

    add_river(first)

    while True:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLUMNS - 1)
        if first[r][c] == TREE:
            first[r][c] = FIRE
            break

    console = Console(width=120)

#----------------------------------------------------------------------------------------------------#

    while is_fire_burning(first):
        max_fire = max(max_fire, count_cells(first, FIRE))
        max_tree = max(max_tree, count_cells(first, TREE))
        total_tree += count_cells(first, TREE)
        total_fire += count_cells(first, FIRE)

        avg_tree = total_tree / step
        avg_fire = total_fire / step

        print("\033[H\033[2J", end="")
        console.print(create_dashboard(first, step, max_fire, max_tree, avg_tree, avg_fire))

        time.sleep(SLEEP_TIME)
        first = update_forest(first)
        step += 1

    max_fire = max(max_fire, count_cells(first, FIRE))
    max_tree = max(max_tree, count_cells(first, TREE))
    total_tree += count_cells(first, TREE)
    total_fire += count_cells(first, FIRE)

    avg_tree = total_tree / step
    avg_fire = total_fire / step

    print("\033[H\033[2J", end="")
    console.print(create_dashboard(first, step, max_fire, max_tree, avg_tree, avg_fire))

#----------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()