# coding=utf-8
def game_loop():
    # The game should run until we return
    while True:
        print_board()

        current_player = get_current_player()

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full():
            # Game over baby
            print('The board is full and nobody won')
            return
        else:
            print("Nobody has won yet, keep looping")


BOARD = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board():
    for row in BOARD:
        print(row)


def get_current_player():
    current_player = raw_input('whose turn is it?\n')
    return current_player


def get_coordinates():
    x_coord = int(raw_input('which column?\n'))
    y_coord = int(raw_input('which row?\n'))
    return [x_coord, y_coord]


def check_place_already_taken(x, y):
    if BOARD[x][y] != '-':
        token = 0
    else:
        token = 1
    return token


def place_token(token, x_coord, y_coord):

    token = check_place_already_taken(x_coord, y_coord)
    if token == 1:
        BOARD[x_coord][y_coord] = token
    else:
        print("Place already taken, enter a new row/column")

def did_win(player):
    player_has_won = False
    for row in BOARD:
        if row[0] == player and row[1] == player and row[2] == player:
            player_has_won = True

    return player_has_won


def is_board_full():
    board_is_full = False
    for row in BOARD:
        if row[0] != '-' and row[1] != '-' and row[2] != '-':
            board_is_full = True

    return board_is_full


def is_legal_move(token, x_coord, y_coord):
    # TODO this should probably be used somewhere...
    raise NotImplementedError


# Run the program
game_loop()
