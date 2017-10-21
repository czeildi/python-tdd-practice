from game_of_life_v2 import game_of_life

def test_game_of_life_exists():
    game_of_life()

def test_gol_accepts_alive_param():
    game_of_life(alive = [])

def test_gol_nobody_borns_from_nothing():
    assert len(game_of_life(alive = [])) == 0