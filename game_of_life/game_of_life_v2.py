def game_of_life(alive = []):
    newborns = borning_cells(alive)
    staying_alive = next_living_from(cells = alive, alive = alive, valid_neighbor_counts = [2, 3])
    return newborns + staying_alive

def borning_cells(alive):
    neighbors_of_alive = ['0, 0']
    return next_living_from(neighbors_of_alive, alive, [3])

def next_living_from(cells, alive, valid_neighbor_counts):
    return [c for c in cells if len(living_neighbors(c, alive)) in valid_neighbor_counts]

def living_neighbors(cell, alive):
    return [c for c in alive if c != cell and are_cells_close(c, cell)]

def are_cells_close(c1, c2):
    close_in_0th = distance_in_nth_direction(c1, c2, 0) <= 1
    close_in_1st = distance_in_nth_direction(c1, c2, 1) <= 1
    return close_in_0th and close_in_1st

def distance_in_nth_direction(c1, c2, n):
    return abs(nth_coord_of_cell(c1, n) - nth_coord_of_cell(c2, n))

def nth_coord_of_cell(cell, n):
    return int(cell.split(', ')[n])
