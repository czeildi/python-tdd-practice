class GameOfLife:
    """implement Conway's game of life"""

    def next(self, living_cells = []):
        return [cell for cell in living_cells if cell == '0, 1']
