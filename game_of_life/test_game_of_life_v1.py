import unittest

from game_of_life_v1 import GameOfLife

class GameOfLifeTest(unittest.TestCase):
    """test Conway's game of life"""
    def test_class_exists(self):
        game = GameOfLife()
        self.assertEqual(game, game)

    def test_next_method_exists(self):
        game = GameOfLife()
        game.next()

    def test_next_operates_on_list_of_living_cells(self):
        game = GameOfLife()
        game.next([])

    def test_next_returns_living_cells(self):
        game = GameOfLife()
        self.assertEqual(game.next([]), [])

    def test_middle_cell_in_row_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '0, 1', '0, 2']
        self.assertTrue('0, 1' in game.next(initial_cells))

    def test_all_but_periferial_cells_stay_alive_in_row(self):
        game = GameOfLife()
        next_cells = game.next(['0, 0', '0, 1', '0, 2', '0, 3', '0, 4'])
        self.assertTrue('0, 1' in next_cells and '0, 2' in next_cells and '0, 3' in next_cells)

    def test_cells_with_no_immediate_neighbors_die(self):
        game = GameOfLife()
        next_cells = game.next(['0, 0', '0, 1', '0, 2', '0, 4'])
        self.assertTrue('0, 1' in next_cells and '0, 2' not in next_cells)

    def test_cell_with_neighbors_in_l_shape_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '1, 0', '0, 1']
        self.assertTrue('0, 0' in game.next(initial_cells))

    def test_cell_with_two_neighbors_in_corner_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '-1, -1', '1, 1']
        self.assertEqual(game.next(initial_cells), ['0, 0'])
    
    def test_cell_with_two_neighbors_in_other_corner_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '-1, 1', '1, -1']
        self.assertEqual(game.next(initial_cells), ['0, 0'])
    
    def test_cell_with_two_neighbors_below_and_above_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '-1, 0', '1, 0']
        self.assertTrue('0, 0' in game.next(initial_cells))

    def test_cell_with_three_neighbors_stays_alive(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '-1, 0', '1, 0', '0, 1']
        self.assertTrue('0, 0' in game.next(initial_cells))

    def test_cell_with_more_neighbors_die_of_overpopulation(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '1, 0', '0, 1', '-1, 0', '0, -1']
        self.assertFalse('0, 0' in game.next(initial_cells))

    def test_origo_borns_if_three_neighbors(self):
        game = GameOfLife()
        initial_cells = ['1, 1', '0, -1', '-1, 1']
        self.assertTrue('0, 0' in game.next(initial_cells))

    def test_return_living_cells_only_once(self):
        game = GameOfLife()
        next_cells = game.next(['0, 0', '1, 1', '0, -1', '-1, 1'])
        self.assertEqual(len([c for c in next_cells if c == '0, 0']), 1)

    def test_other_cell_borns_with_three_neighbors(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '1, 0', '0, 1']
        self.assertTrue('1, 1' in game.next(initial_cells))

    def test_another_cell_borns_with_three_neighbors(self):
        game = GameOfLife()
        initial_cells = ['10, 10', '11, 10', '10, 11']
        self.assertTrue('11, 11' in game.next(initial_cells))

    def test_beacon(self):
        game = GameOfLife()
        initial_cells = ['0, 0', '0, -1', '1, 0', '1, -1', '-1, 1', '-1, 2', '-2, 1', '-2, 2']
        self.assertEqual(initial_cells.sort(), game.next(game.next(initial_cells)).sort())


if __name__ == '__main__':
    unittest.main()
