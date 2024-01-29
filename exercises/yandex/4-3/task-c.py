# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/tQJuwijGwX

def make_equation(*args):
    if len(args) == 1:
        return f'{args[0]}'

    length = len(args) - 1

    return f'({make_equation(*args[:length])}) * x + {args[length]}'
