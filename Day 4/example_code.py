import numpy as np
bingo_calls = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
               10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

# Read in Data
with open(r"C:\Users\Cherry\Desktop\Programming\Advent_Of_Code\Day 4\example_data.txt") as file:
    data = file.read()

# data_str = str(data)
board_rows = [x for x in data.splitlines() if x]
board_rows_cleaned = []

for row in board_rows:
    entry = row.split(' ')
    non_null_entries = [int(x) for x in entry if x != '']
    board_rows_cleaned.append(non_null_entries)


board_list = [board_rows_cleaned[i:i+5]
              for i in range(0, len(board_rows_cleaned), 5)]

player_board = np.array(board_list)
print(player_board.shape)
check_board = np.zeros((3, 5, 5), int)

# Functions


def check_row_bingo(board):
    for rnum in range(0, 5):
        if board[rnum, :].tolist() == [1, 1, 1, 1, 1]:
            return True
    return False


def check_col_bingo(board):
    for cnum in range(0, 5):
        if board[:, cnum].tolist() == [1, 1, 1, 1, 1]:
            return True
    return False


def winning_board(player_boards, check_boards, bingo_calls):
    for call in bingo_calls:
        for idx, board in enumerate(player_boards):
            position = np.argwhere(board == call)
            if position.tolist():
                check_boards[idx][position[0][0]][position[0][1]] = 1

            if check_row_bingo(check_boards[idx]) or check_col_bingo(check_boards[idx]):
                return call, board, check_board[idx]

    return ("No Winnning Board")


call_val, win_board, win_check_board = winning_board(
    player_board, check_board, bingo_calls)


# print(np.argwhere(win_check_board == 1))
index_list_transposed_umarked = np.argwhere(win_check_board == 0).T.tolist()


marked_sum = np.sum(win_board[tuple(index_list_transposed_umarked)])

print(marked_sum*call_val)
