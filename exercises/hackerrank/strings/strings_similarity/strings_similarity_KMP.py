import time

start_time = time.time()


def string_similarity(s):
    i = 1
    j = 0
    p = [0] * len(s)
    num = [str(i) for i in range(0, len(s))]
    show = [" "] * len(s)
    while i < len(s):
        show[i] = 'i'
        show[j] = 'j'
        print(num)
        print(show)
        print(list(s))
        print([str(i) for i in p])
        # print("i = ", i)
        # print("j = ", j)
        print()
        show[i] = ' '
        show[j] = ' '
        if s[i] == s[j]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    print(num)
    print(show)
    print(list(s))
    print([str(i) for i in p])
    # print("i = ", i)
    # print("j = ", j)
    return print(p), print(sum(p))


string_similarity('ababacababab')
print(str)
print(str)
#
# if __name__ == '__main__':
#     s = ''
#     result = ''
#     with open('input2.txt') as f:
#         lines = f.read().splitlines()
#
#         with open('output.txt', 'w') as fr:
#             for i in range(1, len(lines), 1):
#                 s = lines[i]
#
#                 result = string_similarity(s)
#
#                 fr.write(str(result) + '\n')
#
#     expected_lines = []
#     with open('expected2.txt') as f:
#         expected_lines.extend(f.readlines())
#
#     actual_lines = []
#     with open('output.txt') as fr:
#         actual_lines.extend(fr.readlines())
#
#     for i in range(0, len(expected_lines)):
#         al = actual_lines[i]
#         el = expected_lines[i]
#         print(al == el)
#
# print("--- %s seconds ---" % (time.time() - start_time))
