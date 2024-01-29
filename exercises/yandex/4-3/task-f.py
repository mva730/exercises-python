# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/NifdzvxY59

def merge_sort(a):
    n = len(a)
    if n < 2:
        return a

    left = merge_sort(a[:n // 2])
    right = merge_sort(a[n // 2:n])

    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1

    return res
