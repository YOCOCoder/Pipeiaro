class Pipeiaro:

    # root_count
    # stones_count

    def __init__(self):
        self.plant_symbol = '▒'
        self.empty_symbol = ' '

    def generate_grid(self,width = 14, height = 14, empty_symbol = ' '):
        self.grid = []
        for row in range(0,height,1):
            self.grid.append([])
        # print(self.grid)
        for col in self.grid:
            for i in range(0,width,1):
                col.append([empty_symbol])

    def generate_plant(self,left = 5, top = 5, width = 4, height = 4, plant_symbol  = '▒'):
        for row in range(left-1,(left + height-1),1):
            for col in range(left - 1, (top + width - 1), 1):
                self.grid[row][col] = [plant_symbol]

    def printgrid(self):
        try:
            for row in self.grid:
                print(row)
        except:
            print('Grid is empty!')

    def get_start_possible_locations(self):
        self.allowed_startpos = []
        for i, row in enumerate(self.grid,0):
            for j, col in enumerate(row,0):
                if col == [self.plant_symbol]:
                    self.allowed_startpos += self.check_neibrhood(i,j)

        for pos in self.allowed_startpos:
            print(pos)

    def check_neibrhood(self,row,col):
        # Returns list of addresses [i][j] of nearby empty cells
        neibrhood_list = []
        # Out of array check
        min = 0
        max_row = len(self.grid) - 1
        max_col = len(self.grid[0]) - 1

        if row != min:
            neibrhood_list += self.check_empty(row-1,col) # Check UP
        if row != max_row:
            neibrhood_list += self.check_empty(row+1,col) # Check DOWN
        if col != min:
            neibrhood_list += self.check_empty(row,col-1) # Check LEFT
        if col != max_col:
            neibrhood_list += self.check_empty(row,col+1) # Check RIGHT

        return neibrhood_list

    def check_empty(self,row,col):
        if self.grid[row][col] == [self.empty_symbol]:
            return [[[row],[col]]]
        else:
            return []

    def generate_pipes(self):
        pass




ppr = Pipeiaro()
ppr.generate_grid(12,12)
ppr.generate_plant(5,5,4,4)
ppr.get_start_possible_locations()
ppr.printgrid()








