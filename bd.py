from bt import sudoku_in
import time
import random
class make:
    
    def __init__(self) -> None:
       
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.mode = None
        self.solved_board = None
        self.emptied_value = []
    def cheat(self, board):
        soduku = sudoku_in(board)
        soduku.validate()
        return soduku.get_solved()

    def get_board_data(self):
        return self.board
    def get_board_solved_data(self):
        return self.solved_board

                
    def set_mode(self, mode):
        self.mode = mode
    def insert_value(self, row, column, value):
        if [row, column] in self.emptied_value:
            self.data = self.board[row][column] = value
            return True
        return False
    def complete(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == 0:
                    return False
        return True
    def correct(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] != self.solved_board[i][j]:
                    return False
        return True

        
    def create_board(self):
        a=[]
        n = None
        for j in range(0,3):
            for k in range(0,3):
                n = random.randint(1, 9)
                while n in a:
                    n = n+1
                    if n>9:
                        n=1
                    if n not in a:
                        break
                    
                a.append(n)
                self.board[j][k] = n
        soduku = sudoku_in(self.board)
        soduku.validate()
        self.board = soduku.get_solved()
        self.solved_board = soduku.get_solved()
        self.set_value()

        return False


    def set_value(self):
        if self.mode == 'easy':
            val = (81//3)+3
        elif self.mode == 'medium':
            val = 81//2
        elif self.mode == 'hard':
            val = 81-(81//3)
        for i in range(0, val):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            while [row, column] in self.emptied_value:
                row = random.randint(0, 8)
                column = random.randint(0, 8)
                if [row, column] not in self.emptied_value:
                    break
                
            self.emptied_value.append([row,column])
            self.board[row][column] = 0
        return False
