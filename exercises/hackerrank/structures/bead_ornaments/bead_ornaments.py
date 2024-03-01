#!/bin/python3
import itertools

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#

letters = list('abcdefghij')
numbers = list(range(1, 31))


def beadOrnaments(b):
    groups = []
    for i in range(len(b)):
        group = []
        for j in range(b[i]):
            group.append(letters[i] + str(numbers[j]))

        groups.append(list(itertools.permutations(group)))

    r2 = list(itertools.product(*groups))

    return r2


beadOrnaments([2, 2])

# if __name__ == '__main__':
#     result = ''
#     with open('input.txt') as f:
#         lines = f.read().splitlines()
#
#         with open('output.txt', 'w') as fr:
#             for i in range(1, len(lines) - 1, 2):
#                 b_count = lines[i]
#                 b = lines[i + 1]
#
#                 result = beadOrnaments(b)
#
#                 fr.write(result + '\n')
