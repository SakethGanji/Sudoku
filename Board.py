import random
import numpy as np


# populates a row in random spaces
def populate():
    row = [0] * 9
    num_in_box = random.randint(3, 6)
    while True:
        spot = random.randint(0, 8)
        r = random.randint(1, 9)
        if r not in row:
            row[spot] = r
        if row.count(0) == (9 - num_in_box):
            break
    return row


# checks every number in column and row and returns numbers in list
def col_row_nums(array, row, col):
    check_col = [j for j in array[:, col] if j != 0]
    check_row = [i for i in array[row] if i != 0]
    if array[row][col] in check_col:
        check_col.remove(array[row][col])
    return check_col + check_row


# checks every number box and returns numbers in list
def box_nums(array, box_row):
    reshaped_box = np.reshape(array, (27, 3))
    list_boxes_in_rows = list()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                p2 = list(np.reshape((reshaped_box[c::3]), (3, 9)))
                for d in range(3): list_boxes_in_rows.append(p2[a])
    array_boxes_in_rows = np.array(list_boxes_in_rows)
    return [k for k in array_boxes_in_rows[box_row] if k != 0]


# removes any duplicates so each column, row and box all have only one set of numbers 1 - 9
def finalize_board(array):
    box_rows_num = -1
    for x in range(9):
        for y in range(9):
            box_rows_num += 1
            arr = np.array(array)
            possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            col_row_duplicates = list()
            box_duplicates = list()
            used_nums = set(col_row_nums(arr, x, y)) | set(box_nums(arr, box_rows_num))

            for w in used_nums:
                col_row_count = col_row_nums(arr, x, y).count(w)
                box_count = box_nums(arr, box_rows_num).count(w)
                if col_row_count > 1: col_row_duplicates.append(w)
                if box_count > 1: box_duplicates.append(w)
            remaining_nums = list(set(possible_nums) - set(used_nums))

            if array[x][y] in col_row_duplicates or array[x][y] in box_duplicates:
                if len(remaining_nums) > 0:
                    array[x][y] = random.choice(remaining_nums)

    return array


mapped = list()
for x in range(9): mapped.append(populate())
board = finalize_board(mapped)
print(board)
