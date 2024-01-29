# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/xBEkgsU8PR

def cycle(arr):
    while True:
        for i in range(0, len(arr)):
            yield arr[i]
