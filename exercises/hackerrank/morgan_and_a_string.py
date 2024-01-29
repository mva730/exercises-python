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


if __name__ == '__main__':
    fptr = open('./output.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morgan_and_string2(a, b)

        fptr.write(result + '\n')

    fptr.close()
