def longestCommonPrefix(strs):
    pref = set()

    smallest_length = min(map(len, strs))

    for i in range(smallest_length):
        for j in range(len(strs)):
            pref.add(strs[j][i])
            if len(pref) > 1:
                if i == 0:
                    return ""
                return strs[0][:i]
        pref.clear()

    return strs[0][:smallest_length]


print(longestCommonPrefix(["ab", "a"]))
