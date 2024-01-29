# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/SD8Bvedmxs

def make_linear(a):
    if not isinstance(a, list):
        return a
    cont = []
    for i in range(0, len(a)):
        result = make_linear(a[i])

        if type(result) is int:
            cont.append(result)
        else:
            cont.extend(result)
    return cont
