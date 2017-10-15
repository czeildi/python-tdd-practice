class GameOfLife:
    """implement Conway's game of life"""

    def next(self, living_cells = []):
        cells_remaining_alive = self.cellsRemainingAlive(living_cells)
        borning_cells = self.borningCells(living_cells)
        return list(set(cells_remaining_alive + borning_cells))
    
    def cellsRemainingAlive(self, living_cells):
        return [c for c in living_cells if self.cellRemainsAlive(living_cells, c)]
    
    def borningCells(self, living_cells):
        possible_newborns = self.neighborsOfAnyLiving(living_cells)
        return [c for c in possible_newborns if self.cellBorns(living_cells, c)]
    
    def cellRemainsAlive(self, living_cells, cell):
        return self.numOfLivingNeighbors(living_cells, cell) in (2, 3)
    
    def cellBorns(self, living_cells, cell):
        return self.numOfLivingNeighbors(living_cells, cell) == 3
    
    def neighborsOfAnyLiving(self, living_cells):
        neighbor_lists = [self.neighbors(c) for c in living_cells]
        return [c for neighbors in neighbor_lists for c in neighbors]
    
    def numOfLivingNeighbors(self, living_cells, cell):
        living_neigbors = [c for c in self.neighbors(cell) if c in living_cells]
        return len(living_neigbors)
    
    def neighbors(self, cell):
        directions = [[1, 0], [0, -1], [0, 1], [-1, 0],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]
        return [self.neighborInDirection(cell, x, y) for (x, y) in directions]

    def neighborInDirection(self, cell, xShift, yShift):
        (x, y) = self.coordsOfCell(cell)
        return self.cellOfCoords(x + xShift, y + yShift)

    def coordsOfCell(self, cell):
        return [int(coord) for coord in cell.split(', ')]

    def cellOfCoords(self, x, y):
        return str(x) + ', ' + str(y) 
