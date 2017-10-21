def game_of_life(alive = []):
    return [c for c in alive if len(living_neighbors(c, alive)) in [2, 3]]

def living_neighbors(cell, alive):
    return [c for c in alive if c != cell and are_cells_close(c, cell)]

def are_cells_close(c1, c2):
    return x_distance(c1, c2) <= 1

def x_distance(cell_1, cell_2):
    return abs(x_coord_of_cell(cell_1) - x_coord_of_cell(cell_2))

def x_coord_of_cell(cell):
    return int(cell.split(', ')[0])