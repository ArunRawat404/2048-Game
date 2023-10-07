import random


# when game starts
def start_game():
    # a 4*4 matrix with initially all values as 0
    matrix = [[0 for i in range(4)] for i in range(4)]
    return matrix


def add_new_2(matrix):

    # randomly generating 2 coordinate between 0 and 3 including
    x_coordinate = random.randint(0, 3)
    y_coordinate = random.randint(0, 3)

    # checking for empty position
    while matrix[x_coordinate][y_coordinate] != 0:

        x_coordinate = random.randint(0, 3)
        y_coordinate = random.randint(0, 3)

    matrix[x_coordinate][y_coordinate] = 2


# reversing rows of matrix
def reverse(matrix):
    new_matrix = []

    for row in range(4):
        new_matrix.append([])
        for column in range(3, -1, -1):
            new_matrix[row].append(matrix[row][column])

    return new_matrix


# to get the transpose of matrix means interchanging rows and column
def transpose(matrix):
    new_matrix = []

    for row in range(4):
        new_matrix.append([])
        for column in range(4):
            new_matrix[row].append(matrix[column][row])

    return new_matrix


# here we will shift entries of each cell to it's extreme left
def compress(matrix):
    changed = False
    new_matrix = [[0 for i in range(4)] for i in range(4)]

    for row in range(4):
        pos = 0

        for column in range(4):
            if matrix[row][column] != 0:
                # if cell is non-empty then we will shift its number to previous empty cell in that row
                # denoted by pos variable
                new_matrix[row][pos] = matrix[row][column]
                if column != pos:
                    changed = True
                pos += 1

    return new_matrix, changed


# to merge 2 same number which are side by side
def merge(matrix):
    changed = False
    for row in range(4):

        for column in range(3):
            if matrix[row][column] == matrix[row][column + 1] \
                    and matrix[row][column] != 0:
                # merging, double current cell value
                matrix[row][column] = 2 * matrix[row][column]
                # empty the next cell
                matrix[row][column + 1] = 0
                changed = True

    return matrix, changed


# get the current state of the game/matrix (game over/ player wins/ continue playing)
def get_current_state(matrix):

    # if 2048 is present at any position, player won
    for row in range(4):
        for column in range(4):
            if matrix[row][column] == 2048:
                return "Won"

    # if 0 is present at any position, game continues
    for row in range(4):
        for column in range(4):
            if matrix[row][column] == 0:
                return "Game Not Over"

    # if same number is side by side, game continues

    # for every row and column expect last row and last column
    for row in range(3):
        for column in range(3):
            if matrix[row][column] == matrix[row + 1][column]  \
                    or matrix[row][column] == matrix[row + 1][column]:
                return "Game Not Over"

    # for last row
    for column in range(3):
        if matrix[3][column] == matrix[3][column + 1]:
            return "Game Not Over"

    # for last column
    for row in range(3):
        if matrix[row][3] == matrix[row + 1][3]:
            return "Game Not Over"

    # else we have lost the game
    return "Lost"


# function to update the matrix if we move / swipe left
def move_left(matrix):
    new_matrix, changed1 = compress(matrix)
    new_matrix, changed2 = merge(new_matrix)

    changed = changed1 or changed2

    new_matrix, temp = compress(new_matrix)

    return new_matrix, changed


def move_right(matrix):
    new_matrix = reverse(matrix)
    new_matrix, changed = move_left(new_matrix)

    new_matrix = reverse(new_matrix)

    return new_matrix, changed


def move_up(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_left(new_matrix)
    new_matrix = transpose(new_matrix)

    return new_matrix, changed


def move_down(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_right(new_matrix)
    new_matrix = transpose(new_matrix)

    return new_matrix, changed












