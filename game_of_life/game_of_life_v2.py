def game_of_life(alive = []):
    return newborns(alive) + staying_alive(alive)

def newborns(alive):
    return next_living_from(
        cells = neighbors_of_all_alive(alive),
        alive = alive,
        valid_neighbor_counts = [3]
    )

def staying_alive(alive):
    return next_living_from(
        cells = alive,
        alive = alive,
        valid_neighbor_counts = [2, 3]
    )

def next_living_from(cells, alive, valid_neighbor_counts):
    return [c for c in cells if cell_will_live(c, alive, valid_neighbor_counts)]

def cell_will_live(cell, alive, valid_neighbor_counts):
    return len(living_neighbors(cell, alive)) in valid_neighbor_counts

def living_neighbors(cell, alive):
    return [c for c in alive if c != cell and cell in neighbors(c)]

def neighbors_of_all_alive(alive):
    neighbor_lists_of_alive = [neighbors(c) for c in alive]
    return [c for n in neighbor_lists_of_alive for c in n]

def neighbors(cell):
    (x, y) = (nth_coord_of_cell(cell, 0), nth_coord_of_cell(cell, 1))
    return [str(x + dx) + ', ' + str(y + dy) for (dx, dy) in neighbor_steps()]

def nth_coord_of_cell(cell, n):
    return int(cell.split(', ')[n])

def neighbor_steps():
    return [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]
