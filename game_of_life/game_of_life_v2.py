def game_of_life(alive = []):
    return [c for c in alive if len(living_neighbors(c, alive)) == 2]

def living_neighbors(cell, alive):
    return [c for c in alive if c != cell]
