class GameOfLife:
    """implement Conway's game of life"""

    def next(self, living_cells = []):
        return [c for c in living_cells if self.cellRemainsAlive(living_cells, c)]
    
    def cellRemainsAlive(self, living_cells, cell):
        return self.numOfLivingNeighbors(living_cells, cell) >= 2
    
    def numOfLivingNeighbors(self, living_cells, cell):
        living_neigbors = [c for c in self.neighbors(cell) if c in living_cells]
        return len(living_neigbors)
    
    def neighbors(self, cell):
        neighbor_directions = [[1, 0], [0, -1], [0, 1], [-1, 0],
                               [1, 1], [1, -1], [-1, 1], [-1, -1]]
        return [self.neighborInDirection(cell, x, y) for (x, y) in neighbor_directions]

    def neighborInDirection(self, cell, xShift, yShift):
        (x, y) = self.coordsOfCell(cell)
        return self.cellOfCoords(x + xShift, y + yShift)

    def coordsOfCell(self, cell):
        return [int(coord) for coord in cell.split(', ')]

    def cellOfCoords(self, x, y):
        return str(x) + ', ' + str(y) 