import itertools


def alternate(s):
    set_of_chars = set(list(s))
    i = 0

    combos = list(itertools.combinations(set_of_chars, 2))

    container = []
    for combo in combos:
        res = ''
        for ch in s:
            if ch in combo:
                res += ch
        container.append(res)

    cont = container.copy()
    for string in container:
        prev = string[0]
        for i in range(1, len(string)):
            if prev == string[i]:
                cont.remove(string)
                break
            prev = string[i]
            i += 1

    return max(cont, key=len, default=0)

    # strings_container = []
    # for char_to_remove in set_of_chars:
    #     result = []
    #     for ch in list_of_chars:
    #         if char_to_remove != ch:
    #             result.append(ch)
    #
    #     strings_container.append(''.join(result))
    #
    # return strings_container


print(alternate("asdcbsdcagfsdbgdfanfghbsfdab"))
