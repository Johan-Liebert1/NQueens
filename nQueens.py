from printBoard import print_board, write_to_js_file

all_solutions = []

def attack_minor_diagonal(bo, rand_row, rand_col, solving = True):
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


def solve_n_queens(boa, start_col, row):
    if row == board_length:
        if boa not in all_solutions:
            all_solutions.append(boa)
        return True

    start_column = start_col if row == 0 else 0

    for column in range(start_column, board_length):

        if isSafe(boa, row, column):
            boa[row][column] = 'Q'

            if solve_n_queens(boa, start_col, row + 1):
                if boa not in all_solutions:

                    all_solutions.append(boa)
                return True
            

        boa[row][column] = 0

    return False



if __name__ == "__main__":
    board_length = int(input("Enter board dimension > "))

    for i in range(board_length):
        main_board = [[0] * board_length for _ in range(board_length)]

        solve_n_queens(main_board, i, 0)

    for b in all_solutions:
        print_board(b, board_length) 

    write_to_js_file(all_solutions, board_length)