# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/elPWoM9YSV

def recursive_sum(*args):
    if len(args) == 1:
        return args[0]

    length = len(args) - 1

    return args[length] + recursive_sum(*args[:length])
