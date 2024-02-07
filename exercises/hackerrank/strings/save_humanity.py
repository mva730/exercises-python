import re


def kmp_algo(s, pat):
    m = len(pat)
    p = [0] * len(s)

    i = 1
    j = 0
    indeces = []
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

        if j == m:
            indeces.append(i - j - m - 1)
            j = p[j - 1]

    return indeces


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


def compare_indices_at_right(indices, left_part, right_part, original_str):
    length = len(left_part)
    result = []

    for idx in indices:
        res = 0
        mistake = 0

        for i in range(0, len(right_part)):
            if mistake > 1:
                break
            if right_part[i] != original_str[idx + length + i]:
                res += 1
                mistake += 1
            else:
                res += 1

        if res == length:
            result.append(idx)

    return result


def virus_indices(dna, v):
    virus_middle = len(v) // 2

    v_left = v[:virus_middle]
    v_right = v[virus_middle:]

    left_str = v_left + '#' + dna
    right_str = v_right + '#' + dna

    left_indices = kmp_algo(left_str, v_left)
    right_indices = kmp_algo(right_str, v_right)

    left_result = []
    if left_indices:
        left_result = compare_indices_at_right(left_indices, v_left, v_right, dna)

    # right_result = []
    # if right_indices:
    #     right_result = compare_indices(right_indices, v_right, v_left, dna, False)
    #
    # left_result.extend(right_result)

    if not left_result:
        print("No Match!")
    else:
        print(' '.join([str(i) for i in left_result]))


print(virus_indices('aardvark', 'ab'))


def virus_indices_regex(dna, v):
    v_vars = [v[:i] + '.' + v[i + 1:] for i in range(0, len(v))]

    result = []
    for v_var in v_vars:
        regex = f"(?=({v_var}))"
        matches = re.finditer(regex, dna)
        result += [str(match.start(0)) for match in matches]

    result = list(set(result))
    if not result:
        print('No Match!')
    else:
        print(' '.join(sorted(result, key=int)))
