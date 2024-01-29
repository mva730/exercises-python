# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/Dn43U0KwTz

def recursive_digit_sum(n):
    if n == 0:
        return n

    current = n % 10

    return current + recursive_digit_sum(n // 10)
