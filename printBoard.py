import json
from termcolor import colored

def print_board(board, board_length):
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



def write_to_js_file(board, no_of_queens):
    json_board = json.dumps(board)

    with open('scripts/nQueens.js', 'w') as file:
        file.write('const Queens = ')
        file.write(json_board)

    print(colored("SUCCESSFULLY WROTE BOARDS TO JSONBoards.js file", 'green'))
    print("Open view.html to view solutions")