import unittest

from game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):
    """test Conway's game of life"""
    def test_class_exists(self):
        game = GameOfLife()
        self.assertEqual(game, game)

if __name__ == '__main__':
    unittest.main()
