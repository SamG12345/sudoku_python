class sudoku_in:
    
    def __init__(self, data) -> None:
        import copy
        self.data = data
        self.empty_val = []
        self.rc = 0
        self.solved_data = copy.deepcopy(data)


    def validate(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 0:
                    a = [i, j]
                    self.empty_val.append(a)
        self.solve_sudoku()
    

    def check(self, n, row, column):
        for i in range(0, 9):
            if self.solved_data[row][i] == n:
                return False
            if self.solved_data[i][column] == n:
                return False
        row = row - (row % 3)
        column = column - (column % 3)
        for i in range(0, 3):
            for j in range(0, 3):
                if self.solved_data[row + i][column + j] == n:
                    return False
        return True

    def solve_sudoku(self):
        if self.rc >= len(self.empty_val):
            return True

        row, column = self.empty_val[self.rc]

        for i in range(1, 10):
            if self.check(i, row, column):
                self.solved_data[row][column] = i

                self.rc += 1
                if self.solve_sudoku():
                    return True
                
                self.rc -= 1
                self.solved_data[row][column] = 0
                
        return False
    

    def get_solved(self):
        return self.solved_data
    