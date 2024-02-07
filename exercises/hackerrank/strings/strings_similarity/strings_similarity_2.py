import time

start_time = time.time()


def string_similarity(str):
    suffixies = [str[i:] for i in range(0, len(str))]
    result = 0

    for suffix in suffixies:
        if str == suffix:
            result += len(str)
            continue

        if suffix[0] != str[0]:
            continue

        counter = find(suffix, str, 0, len(suffix))
        result += counter

    return result


def find(suffix, str, left_bound, right_bound):
    middle = (right_bound - left_bound) // 2

    left = [left_bound, middle]
    right = [middle + 1, right_bound + 1]

    leftStr = str[left[0]:left[1]]
    leftSuff = suffix[left[0]:left[1]]
    nextToLeftStr = str[left[0]:left[1] + 1]
    nextToLeftSuff = suffix[left[0]:left[1] + 1]
    if leftStr == leftSuff:
        if nextToLeftStr != nextToLeftSuff:
            return left[1]
        return find(suffix, str, right[0], right[1])
    else:
        return find(suffix, str, left[0], left[1])


if __name__ == '__main__':
    s = ''
    result = ''
    with open('input2.txt') as f:
        lines = f.read().splitlines()

        with open('../save_humanity/output.txt', 'w') as fr:
            for i in range(1, len(lines), 1):
                s = lines[i]

                result = string_similarity(s)

                fr.write(str(result) + '\n')

    expected_lines = []
    with open('expected2.txt') as f:
        expected_lines.extend(f.readlines())

    actual_lines = []
    with open('../save_humanity/output.txt') as fr:
        actual_lines.extend(fr.readlines())

    for i in range(0, len(expected_lines)):
        al = actual_lines[i]
        el = expected_lines[i]
        print(al == el)

print("--- %s seconds ---" % (time.time() - start_time))
