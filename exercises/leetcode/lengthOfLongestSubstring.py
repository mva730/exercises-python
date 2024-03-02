def lengthOfLongestSubstringN2(string: str) -> int:
    if not string:
        return 0
    distincts = set()

    r = set()
    for i in range(len(string)):
        j = i

        while j < len(string):
            if string[j] in distincts:
                distincts.clear()
                break

            distincts.add(string[j])
            j += 1

        r.add(j - i)
    return max(r)


# abba

def lengthOfLongestSubstring(string: str) -> int:
    if not string:
        return 0

    distincts = {}
    r = 0
    i = j = 0
    while i < len(string):
        if distincts.get(string[i]) is not None:
            j = max(distincts[string[i]] + 1, j)

        distincts[string[i]] = i
        res = i - j + 1
        if r < res:
            r = res
        i += 1

    return r


print(lengthOfLongestSubstring('abba'))
