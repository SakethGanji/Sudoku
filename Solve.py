import Board
import copy
import random
import numpy as np

checked_board = copy.deepcopy(Board.board)


def finalize_board(array, a):
    box_rows_num = -1
    for x in range(9):
        for y in range(9):
            box_rows_num += 1
            arr = np.array(array)
            possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            col_row_duplicates = list()
            box_duplicates = list()
            used_nums = set(Board.col_row_nums(arr, x, y)) | set(Board.box_nums(arr, box_rows_num))

            for w in used_nums:
                col_row_count = Board.col_row_nums(arr, x, y).count(w)
                box_count = Board.box_nums(arr, box_rows_num).count(w)
                if col_row_count > 1: col_row_duplicates.append(w)
                if box_count > 1: box_duplicates.append(w)
            remaining_nums = list(set(possible_nums) - set(used_nums))
            if a == 0:
                if array[x][y] in col_row_duplicates or array[x][y] in box_duplicates:
                    if len(remaining_nums) > 0:
                        array[x][y] = random.choice(remaining_nums)
            elif a == 1:
                if array[x][y] == 0:
                    for r in remaining_nums:
                        array[x][y] = r
                else:
                    if Board.board[x][y] != array[x][y]:
                        array[x][y] = 0
                        finalize_board(checked_board, 1)
    return array


print(finalize_board(checked_board, 1))
