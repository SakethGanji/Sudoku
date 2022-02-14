import random
import numpy as np

mapped = [[-1] * 9 for x in range(9)]


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


# populates a row in random spaces
def populate(array):
    for x in range(9):
        possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for y in range(9):
           #there is a problem calling col_row_set and box_set
            col_row_set = set(col_row_nums(array, x, y))
            box_set = set(box_nums(array, (x + y)))
            while True:
                cell = random.choice(possible_nums)
                if cell not in (col_row_set + box_set):
                    array[x][y] = cell
                    possible_nums.remove(cell)
                    break


populate(mapped)
print(np.array(mapped))
