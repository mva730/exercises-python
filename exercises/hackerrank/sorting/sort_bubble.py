def bubble_sort(a):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
    return a


print(bubble_sort([4, 3, 4, 1, 2, 3, 4]))
