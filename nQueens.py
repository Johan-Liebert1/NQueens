from printBoard import print_board

board_length = 4

main_board = [[0] * board_length for _ in range(board_length)]


def attack_minor_diagonal(bo, rand_row, rand_col, remove = False):
    # Attacked minor diagonal
    # We go down and left, rows are increasing, cols are decreasing
    i = rand_row
    j = rand_col 

    while 0 <= i < board_length  and 0 <= j < board_length:
        if bo[i][j] == 'Q':
            return False

        i += 1
        j -= 1

    # We go up and right 

    i = rand_row
    j = rand_col 
    while 0 <= i < board_length  and 0 <= j < board_length:
        if bo[i][j] == 'Q':
            return False

        i -= 1
        j += 1
    return True


def attack_major_diagonal(bo, rand_row, rand_col, remove = False):
    # We go left and up
    # rows and cols decreasing
    i = rand_row
    j = rand_col

    while 0 <= i < board_length and 0 <= j < board_length:
        if bo[i][j] == 'Q':
            return False

        i -= 1
        j -= 1


    # We go right and down
    # rows and cols increasing

    i = rand_row
    j = rand_col

    while 0 <= i < board_length and 0 <= j < board_length:
        if bo[i][j] == 'Q':
            return False

        i += 1
        j += 1

    return True



def isSafe(board, row, col):
    # check row
    for i in range(board_length):
        if board[row][i] == 'Q':
            return False

    for j in range(board_length):
        if board[j][col] == 'Q':
            return False

    if attack_major_diagonal(board, row, col) is False or attack_minor_diagonal(board, row, col) is False:
        return False

    return True


def solve_n_queens(boa, row):
    if row == board_length:
        return True

    for column in range(board_length):

        if isSafe(boa, row, column):
            boa[row][column] = 'Q'

            if solve_n_queens(boa, row + 1):
                return True
            

        boa[row][column] = 0

    return False

           

if __name__ == "__main__":
    solve_n_queens(main_board, 0)

    print_board(main_board)