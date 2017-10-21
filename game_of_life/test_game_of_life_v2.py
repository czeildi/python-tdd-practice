from game_of_life_v2 import game_of_life

def test_game_of_life_exists():
    game_of_life()

def test_gol_accepts_alive_param():
    game_of_life(alive = [])

def test_gol_nobody_borns_from_nothing():
    assert len(game_of_life(alive = [])) == 0

def test_gol_cell_stays_alive_w_2_neighbors():
    assert '0, 0' in game_of_life(alive = ['0, 0', '1, 0', '-1, 0'])

def test_gol_cell_stays_alive_w_3_neighbors():
    assert '0, 0' in game_of_life(alive = ['0, 0', '1, 0', '-1, 0', '0, -1'])

def test_gol_cell_dies_if_others_are_far():
    assert '0, 0' not in game_of_life(alive = ['0, 0', '2, 0', '0, 3'])

def test_gol_cell_dies_if_others_are_far_behind():
    assert '0, 0' not in game_of_life(alive = ['0, 0', '-2, 0', '0, 3'])

def test_gol_cell_dies_if_others_are_far_above():
    assert '0, 0' not in game_of_life(alive = ['0, 0', '0, 1', '0, 3'])

def test_gol_origo_borns_if_3_neighbors():
    assert '0, 0' in game_of_life(alive = ['1, 0', '1, 1', '0, 1'])

def test_gol_cell_borns_if_3_neighbors():
    assert '5, 5' in game_of_life(['6, 6', '4, 4', '4, 6'])

def test_gol_cell_in_alive_at_most_once():
    next_gen = game_of_life(['6, 6', '4, 4', '4, 6', '5, 5'])
    assert len([c for c in next_gen if c == '5, 5']) <= 1