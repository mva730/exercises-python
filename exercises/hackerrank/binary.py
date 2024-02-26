# https://stackoverflow.com/questions/12144802/finding-multiple-entries-with-binary-search

def search(arr, num):
    arr = sorted(arr)

    l = 0
    r = len(arr)

    while l + 1 < r:
        m = (l + r) // 2

        # LEFT SEARCH: (l, r] arr[m] < num: return r
        if arr[m] < num:
            l = m
        else:  # arr[m] >= num
            r = m

    print(r)


#       0  1  2  3  4  5  6  7
search([1, 2, 3, 3, 3, 4, 6], 3)


def left_to_start_from_search(arr, num):
    arr = sorted(arr)

    result = 0
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) >> 1

        if arr[m] < num:
            l = m + 1
            result = l
        else:  # arr[m] >= num
            r = m - 1
            result = m

    print(result)


#       0    1   2   3   4   5   6   7
left_to_start_from_search([10, 20, 30, 40], 20)

# (l, r] При левом поиске при равенстве искомого элемента NUM элементу массива a[m] (arr[m] >= NUM),
# граница двигается влево (r = m), ищется самое левое вхождение.
# Левая граница всегда будет меньше искомого элемента
# LEFT SEARCH arr[m] < num
#             num > arr[m]
#       0        3           7
#       0  1     3
#          1  2  3

# [l, r) При правом поиске при равенстве искомого элемента NUM элементу массива a[m] (arr[m] <= NUM),
# граница двигается вправо (l = m), ищется самое правое вхождение.
# Правая граница всегда будет больше искомого элемента
# RIGHT SEARCH arr[m] <= num
#              num >= arr[m]
#       0  1  2  3  4  5  6  7
# srch([1, 2, 3, 3, 3, 4, 6], 3)
#       0        3           7
#                3     5     7
#                3  4  5
