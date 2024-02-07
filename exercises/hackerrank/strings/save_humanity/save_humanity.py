def z_algo(s):
    result = length = len(s)
    right = 0
    left = 0
    z = [length]

    for i in range(1, length):
        z.append(0)
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]

    return z


def kmp_algo(s):
    p = [0] * len(s)
    i = 1
    j = 0
    while i < len(s):
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

    return p


def kmp_search(pat, txt):
    r = []
    N = len(txt)
    M = len(pat)
    lps = kmp_algo(pat)
    i = 0
    j = 0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == M:
            r.append(i - j)
            j = lps[j - 1]

    return r


def soft_compare(idx, part_to_compare, original_str, leftPartCompare=True):
    mistake = 0
    res = 0

    if leftPartCompare:
        idx = idx - len(part_to_compare)

    for i in range(0, len(part_to_compare)):
        if part_to_compare[i] == original_str[idx + i]:
            res += 1
        elif part_to_compare[i] != original_str[idx + i] and mistake > 1:
            return -1
        elif part_to_compare[i] != original_str[idx + i]:
            mistake += 1
            res += 1
        if res == len(part_to_compare):
            return idx


def clear_compare(left_idxs, right_idxs, length):
    r = []
    for left_idx in left_idxs:
        for right_idx in right_idxs:
            if right_idx - left_idx == length:
                r.append(left_idx)

    return r


def virus_indices(dna, v):
    if len(v) > len(dna):
        return "No Match!"

    if len(v) == 1:
        r = []
        for i in range(0, len(dna)):
            r += str(i)
        return ' '.join(r)

    virus_middle = len(v) // 2

    v_left = v[:virus_middle]
    v_right = v[virus_middle:]

    left_indices = kmp_search(v_left, dna)
    right_indices = kmp_search(v_right, dna)
    clear_indices = kmp_search(v, dna)

    left_indices = [left_index for left_index in left_indices if
                    left_index + len(v) <= len(dna) and left_index not in clear_indices]
    right_indices = [right_index for right_index in right_indices if
                     right_index - len(v_left) >= 0 and right_index not in clear_indices]

    res = []
    for idx in left_indices:
        r = soft_compare(idx, v_right, dna, False)
        if r != -1:
            res.append(r)

    for idx in right_indices:
        r = soft_compare(idx, v_left, dna, True)
        if r != -1:
            res.append(r)

    res = sorted(list(set(res)))
    if not res:
        return "No Match!"
    else:
        return ' '.join([str(i) for i in res])


# print(virus_indices(
#     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno',
#     'abcdefghijklmnopqrstuvwxyzabcd'))
print(virus_indices('aardvark', 'ab'))
print(virus_indices('banana', 'nan'))

# if __name__ == '__main__':
#     t = int(input().strip())
#     result = []
#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()
#
#         p = first_multiple_input[0]
#
#         v = first_multiple_input[1]
#
#         result.append(virus_indices(p, v))
#     for i in result:
#         print(i)

if __name__ == '__main__':
    s = ''
    result = ''
    with open('input.txt') as f:
        lines = f.read().splitlines()

        with open('output.txt', 'w') as fr:
            for i in range(1, len(lines), 1):
                s = lines[i]
                dna = s.split()[0]
                v = s.split()[1]

                result = virus_indices(dna, v)

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

# def virus_indices_regex(dna, v):
#     v_vars = [v[:i] + '.' + v[i + 1:] for i in range(0, len(v))]
#
#     result = []
#     for v_var in v_vars:
#         regex = f"(?=({v_var}))"
#         matches = re.finditer(regex, dna)
#         result += [str(match.start(0)) for match in matches]
#
#     result = list(set(result))
#     if not result:
#         print('No Match!')
#     else:
#         print(' '.join(sorted(result, key=int)))
