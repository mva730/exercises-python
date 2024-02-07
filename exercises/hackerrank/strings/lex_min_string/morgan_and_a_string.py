# https://www.hackerrank.com/challenges/morgan-and-a-string/problem?isFullScreen=true
#
def morgan_and_string(a, b):
    res = ''
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            res += a[0]
            a = a[1:]
            continue

        if a[0] > b[0]:
            res += b[0]
            b = b[1:]
            continue

        index = 0
        while a[index] == b[index]:
            index += 1
            if len(a) == index and len(a) == index:
                res += a[0]
                a = a[1:]
                break

            if len(a) == index or a[index] < b[index]:
                res += a[0]
                a = a[1:]
                break

            if len(b) == index or a[index] > b[index]:
                res += b[0]
                b = b[1:]
                break

    if len(a) > 0:
        res += a

    if len(b) > 0:
        res += b

    print(res)
    return res


def morgan_and_string2(a, b):
    res = ''
    a += 'z'
    b += 'z'
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1

    print(res)
    return res


# ZZTQLUZ
# EWKGZAM
def morgan_and_string3(a, b):
    res = ''
    a += 'z'
    b += 'z'
    counter = 0
    while len(a) > 1 and len(b) > 1:
        counter += 1
        if a < b:
            res += a[0]
            a = a[1:]
        else:
            res += b[0]
            b = b[1:]

    # return res + a + b
    return res + a[:-1] + b[:-1]


# 'ZZ' > 'ZZTZ' = False
# 'ZZz' > 'ZZTZz' = True
# 'ZZTZZZ' < 'ZZZZTZ' == True
print(morgan_and_string3('ZZ', 'ZZTZ'))
#
# if __name__ == '__main__':
#     a = ''
#     b = ''
#     result = ''
#     with open('input2.txt') as f:
#         lines = f.read().splitlines()
#
#         with open('output.txt', 'w') as fr:
#             for i in range(1, len(lines) - 1, 2):
#                 a = lines[i]
#                 b = lines[i + 1]
#
#                 result = morgan_and_string3(a, b)
#
#                 fr.write(result + '\n')
#
#     expected_lines = []
#     with open('expected.txt') as f:
#         expected_lines.extend(f.readlines())
#
#     actual_lines = []
#     with open('output.txt') as fr:
#         actual_lines.extend(fr.readlines())
#
#     for i in range(0, len(expected_lines)):
#         al = actual_lines[i]
#         el = expected_lines[i]
#
#         if al != el:
#             print(len(el))
#             print(len(el))
#
#             for j in range(0, len(al)):
#                 al_al = al[j]
#                 el_el = el[j]
#
#                 if al_al != el_el:
#                     print(j)
#                     print(al_al)
#                     print(el_el)
