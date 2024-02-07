import time

start_time = time.time()


def string_similarity(str):
    suffixies = [str[i:] for i in range(0, len(str))]
    result = 0
    for suffix in suffixies:
        if str == suffix:
            result += len(str)
            continue

        counter = 0
        for i in range(0, len(suffix)):
            if suffix[i] == str[i]:
                counter += 1
            else:
                break

        result += counter

    return result


print(string_similarity('aabaabaabaaa'))
print(str)

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
