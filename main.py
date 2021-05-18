sudoku_input = [["4", "*", "8", "*", "*", "9", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "8", "*", "6"],
                ["6", "*", "5", "8", "3", "4", "7", "*", "*"],
                ["*", "*", "6", "*", "7", "5", "3", "*", "*"],
                ["*", "3", "*", "*", "1", "*", "*", "8", "*"],
                ["*", "*", "1", "4", "8", "*", "2", "*", "*"],
                ["*", "*", "9", "5", "2", "8", "4", "*", "1"],
                ["7", "*", "2", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "3", "*", "*", "6", "*", "5"]]


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f" {board[r][c]} ", end="")
            if c == 2 or c == 5:
                print("|", end="")
        print()

        if r == 2 or r == 5:
            print("---------+---------+--------")


def squares_to_list(sudoku_unsolved, starting_x, starting_y):
    square_to_list = []
    for y in range(3):
        for x in range(3):
            square_to_list.append(sudoku_unsolved[starting_y + y][starting_x + x])
    return square_to_list


def sudoku_position_to_square_x(position_x):
    if position_x < 3:
        position_x = 0
    if 6 > position_x > 2:
        position_x = 3
    if position_x > 6:
        position_x = 6
    return position_x


def sudoku_position_to_square_y(position_y):
    if position_y < 3:
        position_y = 0
    if 6 > position_y > 2:
        position_y = 3
    if position_y > 6:
        position_y = 6
    return position_y


def sudoku_solver(sudoku_unsolved):
    for r in range(9):
        for c in range(9):
            possible_sudoku_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            possible_numbers = []
            if sudoku_unsolved[r][c] == "*":  # row
                numbers_in_row = list(filter("*".__ne__, sudoku_unsolved[r]))

                cells_in_column = []  # column
                for row in range(9):
                    for cell in sudoku_unsolved[row][c]:
                        cells_in_column.append(cell)
                numbers_in_column = list(filter("*".__ne__, cells_in_column))

                cells_in_square = squares_to_list(sudoku_unsolved, sudoku_position_to_square_x(c),  # square
                                                  sudoku_position_to_square_y(r))
                numbers_in_square = list(filter("*".__ne__, cells_in_square))

                numbers = numbers_in_row + numbers_in_column + numbers_in_square  # all impossible solutions in one list
                for number_1 in possible_sudoku_numbers:
                    if number_1 in numbers:
                        possible_sudoku_numbers = possible_sudoku_numbers
                    if number_1 not in numbers:
                        possible_sudoku_numbers.remove(number_1)
                print(possible_sudoku_numbers)
            # for number in numbers:
            #     if number in numbers:
            #         possible_sudoku_numbers.remove(number)
            # sudoku_unsolved[r][c] = possible_sudoku_numbers


sudoku_solver(sudoku_input)



def sudoku_checker(final_sudoku):
    list_if_true = []
    for r in range(len(final_sudoku)):  # if all elements are different in 1 row
        list_row = list(filter("*".__ne__, final_sudoku[r]))
        if len(set(list_row)) == len(list_row):
            list_if_true.append(1)
        else:
            list_if_true.append(0)

        numbers_1_column = []
        for x in range(9):  # if all elements are different in 1 column
            for number in final_sudoku[x][r]:
                numbers_1_column.append(number)
        list_column = list(filter("*".__ne__, numbers_1_column))
        if len(set(list_column)) == len(list_column):
            list_if_true.append(1)
        else:
            list_if_true.append(0)

    for position_y in [0, 3, 6]:  # if all elements in boxes are different
        for position_x in [0, 3, 6]:
            box_in_list = squares_to_list(final_sudoku, position_x, position_y)
            list_box = list(filter("*".__ne__, box_in_list))
            if len(set(list_box)) == len(list_box):
                list_if_true.append(1)
            else:
                list_if_true.append(0)

    if 0 in list_if_true:
        print("Sudoku is not solvable!")

    else:
        print("Sudoku is solvable!")
    print(list_if_true)

# sudoku_checker(sudoku_input)
