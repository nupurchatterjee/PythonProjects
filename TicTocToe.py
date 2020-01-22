from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('-' + '|' + '-' + '|' + '-' + '|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-' + '|' + '-' + '|' + '-' + '|')
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def place_marker(marker, board, position):
    board[position] = marker


place_marker('$', test_board, 7)

display_board(test_board)


def player_input():
    """OUTPUT : PLAYER 1 marker , player 2 marker    #"""
    marker = ''

    while not (marker == 'X' and marker == 'O'):
        marker = input('Player 1 choose X or O').upper()
        if marker == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'


def choosefirst():
    random_num = random.randint(0, 1)

    if random_num == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def player_choice(board):
    position = 0

    while position not in range(0, 9) or not space_check(board, position):
        position = int(input('Player choice'))

    return position

def replay():

    user_input = input('if you want to play')

    return user_input
