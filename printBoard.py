from termcolor import colored

board_length = 4

def print_board(board):
    string = ''
    for row in range(board_length):
        string += "\n\n"

        for col in range(board_length):
            # 3 spaces between characters

            if board[row][col] == 0:
                string += str(board[row][col]) + '   '

            elif board[row][col] == 'Q':
                string += colored(str(board[row][col]), 'green') + '   '


            else:
                string += colored(str(board[row][col]), 'red') + '   '

    print(string + "\n\n")