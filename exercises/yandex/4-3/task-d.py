# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/pQYOvEFBap

def answer(f):
    def dec(*args, **kwargs):
        return f'Результат функции: {f(*args, **kwargs)}'
    return dec
