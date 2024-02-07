import time

start_time = time.time()


def string_similarity(s):
    l = 0
    r = 0
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        if (i < r):
            z[i] = min(r - i, z[i - l])

        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1

        if (i + z[i] > r):
            l = i
            r = i + z[i]

    return sum(z)


print(string_similarity('baaaaaaaaaa'))


def string_similarity2(s):
    result = length = len(s)
    right = 0
    left = 0
    z = [length]

    for i in range(1, length):
        z.append(0)
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

        result += z[i]

    return result


print(string_similarity2('aaaaaaaaaa'))

if __name__ == '__main__':
    s = ''
    result = ''
    with open('../save_humanity/input.txt') as f:
        lines = f.read().splitlines()

        with open('../save_humanity/output.txt', 'w') as fr:
            for i in range(1, len(lines), 1):
                s = lines[i]

                result = string_similarity(s)

                fr.write(str(result) + '\n')

    expected_lines = []
    with open('../save_humanity/expected.txt') as f:
        expected_lines.extend(f.readlines())

    actual_lines = []
    with open('../save_humanity/output.txt') as fr:
        actual_lines.extend(fr.readlines())

    for i in range(0, len(expected_lines)):
        al = actual_lines[i]
        el = expected_lines[i]
        print(al == el)

print("--- %s seconds ---" % (time.time() - start_time))
