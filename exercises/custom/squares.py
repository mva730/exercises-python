def count_squares(arr):
    i = 0
    j = len(arr) - 1

    r = []
    while i <= j:
        if (left := arr[i] ** 2) > (right := arr[j] ** 2):
            r.append(left)
            i += 1
        elif left < right:
            r.append(right)
            j -= 1
        elif left == right:
            if i != j:
                r.append(left)
                r.append(right)
            else:
                r.append(left)
            i += 1
            j -= 1

    print(r[::-1])


count_squares([-3, -2, 4, 5, 6])
