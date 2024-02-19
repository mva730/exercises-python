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

        print(l, r)

    print(r)


#       0  1  2  3  4  5  6  7
search([1, 2, 3, 3, 3, 4, 6], 3)

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
