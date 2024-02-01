str = 'aaaaaabaa'
suffix = 'aaaaa'


def find(suffix, str, length):
    if str[:length] == suffix[:length]:
        while str[:length] == suffix[:length]:
            length += 1
            return length - 1
    else:
        length = length // 2
        find(suffix, str, length)
    return length


print(find(str, suffix, len(suffix)))
