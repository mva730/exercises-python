def quickSort(a):
    left = []
    equal = []
    right = []
    for el in a:
        if el > a[0]:
            right.append(el)
        if el < a[0]:
            left.append(el)
        if el == a[0]:
            equal.append(el)

    return left + equal + right
