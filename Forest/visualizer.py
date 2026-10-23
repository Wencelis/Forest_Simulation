from rich.panel import Panel
from rich.table import Table
from config import TREE, FIRE, WATER, EMPTY, STATS_BAR_SIZE
from simulation import count_cells

#----------------------------------------------------------------------------------------------------#

def display_forest(forest):
    text_map = ""
    for row in forest:
        for cell in row:
            if cell == TREE:
                text_map += "🌲"
            elif cell == FIRE:
                text_map += "🔥"
            elif cell == WATER:
                text_map += "🟦"
            elif cell == EMPTY:
                text_map += "⬛"
        text_map += "\n"
    return text_map.rstrip("\n") 

#----------------------------------------------------------------------------------------------------#

def display_stats(forest, step, max_fire, max_tree, avg_tree, avg_fire):
    current_fire = count_cells(forest, FIRE)
    current_tree = count_cells(forest, TREE)
    current_water = count_cells(forest, WATER)
    current_empty = count_cells(forest, EMPTY)

    total_cells = len(forest) * len(forest[0])
    tree_blocks = int((current_tree * STATS_BAR_SIZE) / total_cells)
    fire_blocks = int((current_fire * STATS_BAR_SIZE) / total_cells)
    water_blocks = int((current_water * STATS_BAR_SIZE) / total_cells)
    empty_blocks = STATS_BAR_SIZE - (tree_blocks + fire_blocks + water_blocks)

    stats_text = (
        f"Krok symulacji: {step}\n"
        f"Drzewa: {current_tree} | Rekord: {max_tree} | Średnia: {round(avg_tree, 1)}\n"
        f"Ogień:  {current_fire} | Rekord: {max_fire} | Średnia: {round(avg_fire, 1)}\n"
        f"Woda:   {current_water} | Puste: {current_empty}\n\n"
        f"Ekosystem:\n[{'🟩' * tree_blocks}{'🟥' * fire_blocks}{'🟦' * water_blocks}{'⬛' * empty_blocks}]"
    )
    return stats_text

#----------------------------------------------------------------------------------------------------#

def create_dashboard(forest, step, max_fire, max_tree, avg_tree, avg_fire):
    map_text = display_forest(forest)
    stats_text = display_stats(forest, step, max_fire, max_tree, avg_tree, avg_fire)

    map_panel = Panel(map_text, title="Symulacja Lasu", border_style="green")
    stats_panel = Panel(stats_text, title="Statystyki", border_style="blue")

    dashboard = Table.grid(padding=(0, 2))
    dashboard.add_row(map_panel, stats_panel)

    return dashboard