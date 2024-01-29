# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/6O4mmgt83M

def result_accumulator(f):
    result = []

    def dec(*args, method='accumulate'):
        nonlocal result
        result.append(f(*args))
        if method == 'drop':
            temp = result.copy()
            result.clear()
            return temp

    return dec
