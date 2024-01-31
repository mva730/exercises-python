def string_similarity(str):
    suffixies = [str[i:] for i in range(0, len(str))]
    result = 0
    for suffix in suffixies:
        if str == suffix:
            result += len(str)
            continue

        if suffix[0] != str[0]:
            continue

        sub_str = str
        sub_suffix = suffix
        j = 2
        end = len(suffix)
        while sub_str != sub_suffix:
            end = len(sub_str) // j
            sub_str = sub_str[:end]
            sub_suffix = sub_suffix[:end]

        counter = 0
        for i in range(end, len(suffix)):
            if suffix[i] == str[i]:
                counter += 1
            else:
                break

        result += counter + end

    # print(suffixies)
    return result


# string_similarity('ababaa')
# print()
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
