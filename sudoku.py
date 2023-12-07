import random
from bt import sudoku_in
from bd import make

print("------ Welcome to Sudoku game ------")
run = True

bd = make()
def reset():
    bd = None
    bd = make()
def board(data):
        print("     0  1  2     3  4  5     6  7  8")
        print('  |-----------------------------------|')
        for i in range(len(data)):
            if (i % 3) == 0 and i != 0:
                print('  |-----------|-----------|-----------|')
            print(i, end = " " )
            for j in range(len(data[i])):
                if j % 3 == 0:
                    print('|  ', end="")
                print(data[i][j], " ", end="")
            if j == 8:
                print("|")
        print('  |-----------------------------------|')
        return False
def start():
    print("Choose your mode :")
    mode = int(input("1. Easy\t2. Medium\n3. Hard :"))
    if mode == 1:
        mode_set = 'easy'
        bd.set_mode(mode_set)
    elif mode == 2:
        mode_set = 'medium'
        bd.set_mode(mode_set)
    elif mode == 3:
        mode_set = 'hard'
        bd.set_mode(mode_set)
    else:
        print("Invalid input ")
        start()
def play():
    running = True
    while running:
        board(bd.get_board_data())
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        value = int(input("Enter the value to insert: "))         

        if not bd.insert_value(row, column, value):
            if row==111 or column==111 or value == 111:
                print("Cheating........")
                board(bd.cheat(bd.get_board_data()))
                print("")
            else:
                print("Invalid input check the input. ")
        if bd.complete():
            if bd.correct():
                board(bd.get_board_data())
                print("Congratulation you solved the sudoku")
                
                break
                running = False

while run:
    print("1. Start game\t2. exit")
    a = int(input("Enter your choice : "))
    if a==1:
        start()
        bd.create_board()
        play()
        reset()
    elif(a==2):
        run==False
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!!!!")
