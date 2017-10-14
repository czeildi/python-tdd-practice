import unittest

from game_of_life import GameOfLife

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
        
if __name__ == '__main__':
    unittest.main()
