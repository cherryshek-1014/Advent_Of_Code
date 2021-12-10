import numpy as np
bingo_calls = [67, 3, 19, 4, 64, 39, 85, 14, 84, 93, 79, 26, 61, 24, 65, 63, 15, 69, 48, 8, 82, 75, 36, 96, 16, 49, 28, 40, 97, 38, 76, 91, 83, 7, 62, 94, 21, 95, 6, 10, 43, 17, 31, 34, 81, 23, 52, 60,
               54, 29, 70, 12, 35, 0, 57, 45, 20, 71, 78, 44, 90, 2, 33, 68, 53, 92, 50, 73, 88, 47, 58, 5, 9, 87, 22, 13, 18, 30, 59, 56, 99, 11, 77, 55, 72, 32, 37, 89, 42, 27, 66, 41, 86, 51, 74, 1, 46, 25, 98, 80]

# Read in Data
with open(r"C:\Users\Cherry\Desktop\Programming\Advent_Of_Code\Day 4\data.txt") as file:
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
check_board = np.zeros(player_board.shape, int)


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
