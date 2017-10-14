class GameOfLife:
    """implement Conway's game of life"""

    def next(self, living_cells = []):
        return [c for c in living_cells if self.twoLivingNeighbors(living_cells, c)]
    
    def twoLivingNeighbors(self, living_cells, cell):
        left_lives = self.leftNeighborLives(living_cells, cell)
        right_lives = self.rightNeighborLives(living_cells, cell)
        return left_lives and right_lives
    
    def leftNeighborLives(self, living_cells, cell):
        return self.leftNeighbor(cell) in living_cells
    
    def rightNeighborLives(self, living_cells, cell):
        return self.rightNeighbor(cell) in living_cells

    def leftNeighbor(self, cell):
        (x, y) = self.coordsOfCell(cell)
        return self.cellOfCoords(x, y - 1)

    def rightNeighbor(self, cell):
        (x, y) = self.coordsOfCell(cell)
        return self.cellOfCoords(x, y + 1)

    def coordsOfCell(self, cell):
        return [int(coord) for coord in cell.split(', ')]

    def cellOfCoords(self, x, y):
        return str(x) + ', ' + str(y) 