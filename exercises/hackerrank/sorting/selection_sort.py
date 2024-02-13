def selection_sort(arr):
    n = len(arr)

    for k in range(0, n - 1):
        for j in range(k + 1, n):
            if arr[k] > arr[j]:
                arr[j], arr[k] = arr[k], arr[j]
        print(arr)


selection_sort([44, 55, 12, 42, 94, 18, 6, 67])
selection_sort([6, 55, 44, 42, 94, 18, 12, 67])
