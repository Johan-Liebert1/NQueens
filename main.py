from termcolor import colored
import random

board_length = 8

main_board = [['0'] * board_length for _ in range(board_length)]

def print_board(board):
    string = ''
    for row in range(board_length):
        string += "\n\n"

        for col in range(board_length):
            # 3 spaces between characters

            if board[row][col] == '0':
                string += str(board[row][col]) + '   '

            elif board[row][col] == 'Q':
                string += colored(str(board[row][col]), 'green') + '   '


            else:
                string += colored(str(board[row][col]), 'red') + '   '

    print(string + "\n\n")


def attack_minor_diagonal(bo, rand_row, rand_col):
    # Attacked minor diagonal
    # We go down and left, rows are increasing, cols are decreasing
    i = rand_row
    j = rand_col 

    while 0 <= i < board_length  and 0 <= j < board_length:
        # print(f'({i}, {j})', end = " ")

        if bo[i][j] != 'Q':
            bo[i][j] = '1'

        i += 1
        j -= 1

    # We go up and right 

    i = rand_row
    j = rand_col 
    while 0 <= i < board_length  and 0 <= j < board_length:
        if bo[i][j] != 'Q':
            bo[i][j] = '1'

        i -= 1
        j += 1


def attack_major_diagonal(bo, rand_row, rand_col):
    # We go left and up
    # rows and cols decreasing
    i = rand_row
    j = rand_col

    while 0 <= i < board_length and 0 <= j < board_length:
        if bo[i][j] != 'Q':
            bo[i][j] = '1'

        i -= 1
        j -= 1


    # We go right and down
    # rows and cols increasing

    i = rand_row
    j = rand_col

    while 0 <= i < board_length and 0 <= j < board_length:
        if bo[i][j] != 'Q':
            bo[i][j] = '1'

        i += 1
        j += 1


# call it first to place a random queen on board and then go from there
def place_queen(board, i = None, j = None, place_randomly = False):
    if place_randomly:
        rand_row = random.randrange(board_length)
        rand_col = random.randrange(board_length)

    else:
        rand_row = i
        rand_col = j

    
    board[rand_row][rand_col] = 'Q'

    # Attacked spots in columns

    for row in range(board_length):
        if board[row][rand_col] != 'Q':
            board[row][rand_col] = '1'

    # Attacked spots in columns

    for col in range(board_length):
        if board[rand_row][col] != 'Q':
            board[rand_row][col] = '1'

    attack_minor_diagonal(board, rand_row, rand_col)
    attack_major_diagonal(board, rand_row, rand_col)

    
 
def find_unfilled(passed_board):
    for i in range(board_length):
        for j in range(board_length):
            if passed_board[i][j] == '0':
                return i, j
    return False

def isSpotAvailable(passed_board, the_row, the_col):
    if passed_board[the_row][the_col] == '0':
        return True

    return False
   

def solve_n_queens(boa):
    if find_unfilled(boa) is False:
        # means no unfilled spot was found, ie, problem is solved
        return True

    else:
        row, col = find_unfilled(boa)
        print(row, col)

    if isSpotAvailable(boa, row, col):
        place_queen(boa, row, col)

        if solve_n_queens(boa):
            return True

        else:
            boa[row][col] = '0'


place_queen(main_board, place_randomly=True)
# print_board(main_board)
solve_n_queens(main_board)
print_board(main_board)