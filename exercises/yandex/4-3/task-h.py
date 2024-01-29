# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/kp272sXKd0

def fibonacci(n):
    n_0 = 0
    n_1 = 1

    for i in range(0, n):
        yield n_0
        n_0, n_1 = n_1, n_0 + n_1
