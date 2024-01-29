#!/bin/python3


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    height = len(matrix)
    width = len(matrix[0])

    flat_matrix = sum(matrix, [])
    offset = width
    zoom = 0
    first_row = first_column = [0] * 3
    result = []
    while len(first_row) > 2 and len(first_column) > 2:
        first_row = dict([(offset * zoom + i, flat_matrix[offset * zoom + i]) for i in range(zoom, width)][::-1])
        first_column = [(offset * i + zoom, flat_matrix[offset * i + zoom]) for i in range(zoom, height)][1:]
        last_row = [((height - 1) * offset + i, flat_matrix[(height - 1) * offset + i]) for i in range(zoom, width)][1:]
        last_column = [(offset * i + (width - 1), flat_matrix[offset * i + (width - 1)]) for i in range(zoom, height)][
                      ::-1][1:]

        width -= 1
        height -= 1
        zoom += 1

        result.append(first_row + first_column + last_row + last_column)

    rounds = []
    for res in result:
        rnd = res
        result_round = rnd.copy()

        for i in range(0, len(rnd)):
            index = i + r
            if index >= len(rnd):
                index = index % len(rnd)

            element_to_update = rnd[index]
            element_to_move = rnd[i]
            result_round[index] = (element_to_update[0], element_to_move[1])

        rounds.append(result_round)

    result = []
    for rnd in rounds:
        result.extend(rnd)

    sorted_rounds = sorted(result)
    splitted = [sorted_rounds[i:i + offset] for i in range(0, len(sorted_rounds), offset)]

    for i, item in enumerate(splitted):
        for j, el in enumerate(item):
            print(splitted[i][j])
            splitted[i][j] = el[1]

    print('\n'.join([' '.join([(str(i)) for i in item]) for item in splitted]))
    # 1  2  3  4
    # 7  8  9  10
    # 13 14 15 16
    # 19 20 21 22
    # 25 26 27 28
    # 1st row [0, width] ... [0, 2] [0, 1] [0, 0]
    # 1st column [height, 0] ... [2, 0] [1, 0] [0, 0]
    # last row [height, 0] ... [height, width-2] [height, width-1] [height, width]
    # last column [height, width] ... [2, width] [1, width] [0, width]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
