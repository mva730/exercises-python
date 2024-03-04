def longestPalindromeLinear(self, s: str) -> str:
    r = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                r[len(s[i:j + 1])] = s[i:j + 1]

    return r[max(r)]


def longestPalindrome(s: str):
    if len(s) == 1:
        return s

    r = {}

    possibleEven = []
    possibleOdd = []

    i = 0
    while i >= 0 and i + 1 < len(s):
        if s[i] == s[i + 1]:
            possibleEven.append(i)
            r[len(s[i:i + 2])] = s[i:i + 2]
        i += 1

    i = 1
    while i - 1 >= 0 and i + 1 < len(s):
        if s[i - 1] == s[i + 1]:
            possibleOdd.append(i)
            r[len(s[i - 1:i + 2])] = s[i - 1:i + 2]

        i += 1

    for idx in possibleEven:
        current = idx
        local_result = ""
        k = 1
        while (left := current - k) >= 0 and (right := current + k + 1) < len(s):
            if s[left:right + 1] == s[left:right + 1][::-1]:
                local_result = s[left:right + 1]
            else:
                break
            k += 1

        if local_result:
            r[len(local_result)] = local_result

    for idx in possibleOdd:
        current = idx
        local_result = ""
        k = 1
        while (left := current - k) >= 0 and (right := current + k) < len(s):
            if s[left:right + 1] == s[left:right + 1][::-1]:
                local_result = s[left:right + 1]
            else:
                break
            k += 1

        if local_result:
            r[len(local_result)] = local_result

    if r:
        return r[max(r)]
    else:
        return s[0]


def longestPalindromeBad(s: str) -> str:
    if s == s[::-1]:
        return s

    if len(s) == 1:
        return s

    res = {}
    i = 0
    while i < len(s):
        j = i + 1
        if s[i:j] == s[i:j][::-1]:
            # spread right
            while j <= len(s) and s[i:j] == s[i:j][::-1]:
                j += 1
            j -= 1
            # spread both
            while i > 0 and s[i:j] == s[i:j][::-1]:
                i -= 1
                j += 1

            if s[i:j] != s[i:j][::-1]:
                i += 1
                j -= 1

            res[len(s[i:j])] = s[i:j]

        i += 1

    return res[max(res)]
