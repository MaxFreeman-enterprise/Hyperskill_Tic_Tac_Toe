import re


def pretty_board(board: str) -> str:
    b = board.replace("_", " ")
    return f"""---------
| {b[0]} {b[1]} {b[2]} |
| {b[3]} {b[4]} {b[5]} |
| {b[6]} {b[7]} {b[8]} |
---------"""


def game_state(board: str) -> str:
    if re.search("XXX......", board) or re.search("...XXX...", board) or re.search("......XXX", board) or \
            re.search("X..X..X..", board) or re.search(".X..X..X.", board) or re.search("..X..X..X", board) or \
            re.search("X...X...X", board) or re.search("..X.X.X..", board):
        return "X wins"

    elif re.search("OOO......", board) or re.search("...OOO...", board) or re.search("......OOO", board) or \
            re.search("O..O..O..", board) or re.search(".O..O..O.", board) or re.search("..O..O..O", board) or \
            re.search("O...O...O", board) or re.search("..O.O.O..", board):
        return "O wins"

    elif "_" in board:  # board.find("_") > -1:
        return "Game not finished"

    else:
        return "Draw"


def is_empty_square(board_array: [[str]], row: int, col: int) -> bool:
    return board_array[row][col] == "_"


# returns a list of free [(row, col)]
def get_free_coordinates(board_array: [[str]]) -> [(int, int)]:
    res = []
    for i, row in enumerate(board_array):
        for j, cell in enumerate(row):
            if is_empty_square(board_array, j, i):
                res.append((i, j))
    return res


def update_board_array(board_array: [[str]], row: int, col: int, turn: str) -> bool:
    if is_empty_square(board_array, row, col):
        board_array[row][col] = turn
        return True
    else:
        return False


def transform_user_coordinates(user_row: int, user_col: int) -> (int, int):
    return 3-user_row, user_col-1


def make_board_string(board_array: [[str]]) -> str:
    return "".join(["".join(x) for x in board_array])


def switch_turn(current_turn: str):
    return "O" if current_turn == "X" else "X"


current_board = "_________"
board_array = [list(current_board[0:3]), list(current_board[3:6]), list(current_board[6:9])]
current_turn = "X"

print(pretty_board(current_board))

while True:
    while True:
        coords = input("Enter the coordinates: > ").split()
        y, x = coords if len(coords) == 2 else ("@", "@")
        if not x.isnumeric() or not y.isnumeric():
            print("You should enter numbers!")

        elif not (1 <= int(x) <= 3) or not (1 <= int(y) <= 3):
            print("Coordinates should be from 1 to 3!")

        elif not is_empty_square(board_array, *transform_user_coordinates(int(x), int(y))):
            print("This cell is occupied! Choose another one!")

        else:
            if update_board_array(board_array, *transform_user_coordinates(int(x), int(y)), current_turn):
                break

    current_board = make_board_string(board_array)
    print(pretty_board(current_board))

    if game_state(current_board) != "Game not finished":
        print(game_state(current_board))
        break

    current_turn = switch_turn(current_turn)
