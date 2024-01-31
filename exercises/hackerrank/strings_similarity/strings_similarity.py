def string_similarity(str):
    suffixies = [str[i:] for i in range(0, len(str))]
    result = 0
    for suffix in suffixies:
        if str == suffix:
            result += len(str)
            continue

        # j = 0
        # check = suffix
        # while (ind := str.find(check)) != 0 and j < len(suffix):
        #     j += 1
        #     check = check[:-j]
        # else:
        #     result += len(check)

        for i in range(1, len(suffix)):
            if suffix[i] == str[i]:
                result += len(suffix)
            else:
                break

    # print(suffixies)
    return result


string_similarity('ababaa')
print()
if __name__ == '__main__':
    s = ''
    result = ''
    with open('input.txt') as f:
        lines = f.read().splitlines()

        with open('output.txt', 'w') as fr:
            for i in range(1, len(lines), 1):
                s = lines[i]

                result = string_similarity(s)

                fr.write(str(result) + '\n')

    expected_lines = []
    with open('expected.txt') as f:
        expected_lines.extend(f.readlines())

    actual_lines = []
    with open('output.txt') as fr:
        actual_lines.extend(fr.readlines())

    for i in range(0, len(expected_lines)):
        al = actual_lines[i]
        el = expected_lines[i]
        print(al == el)
