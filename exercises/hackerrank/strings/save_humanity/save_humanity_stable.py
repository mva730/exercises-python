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


def compare_left_part(idx, shift, part_to_compare, original_str):
    mistake = 0
    res = 0
    for i in range(0, len(part_to_compare)):
        if mistake > 1:
            break
        if part_to_compare[i] == original_str[idx + shift + i]:
            res += 1
        else:
            mistake += 1
            if mistake < 2:
                res += 1

    if res == len(part_to_compare):
        return idx


def compare_right_part(idx, shift, part_to_compare, original_str):
    mistake = 0
    res = 0
    for i in range(0, len(part_to_compare)):
        if part_to_compare[i] == original_str[idx - shift + i]:
            res += 1
        else:
            mistake += 1
            if mistake < 2:
                res += 1
            else:
                break

    if res == len(part_to_compare):
        return idx - len(part_to_compare)


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

    # TODO check dynamic list changes
    li = []
    for i in range(0, len(left_indices)):
        if left_indices[i] + len(v_left) + len(v_right) <= len(dna):
            li.append(left_indices[i])

    ri = []
    for i in range(0, len(right_indices)):
        if right_indices[i] - len(v_left) >= 0:
            ri.append(right_indices[i])

    res = []
    for idx in li:
        r = compare_left_part(idx, len(v_left), v_right, dna)
        if r is not None:
            res.append(compare_left_part(idx, len(v_left), v_right, dna))

    for idx in ri:
        r = compare_right_part(idx, len(v_right), v_left, dna)
        if r is not None:
            res.append(compare_right_part(idx, len(v_right), v_left, dna))

    res = sorted(list(set(res)))
    if not res:
        return "No Match!"
    else:
        return ' '.join([str(i) for i in res])


if __name__ == '__main__':
    t = int(input().strip())
    result = []
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]

        result.append(virus_indices(p, v))
    for i in result:
        print(i)
