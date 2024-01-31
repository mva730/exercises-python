def quick_sort(arr, hi, lo):
    if hi - lo < 1:
        return

    pivot = arr[hi]
    left_index = lo
    for i in range(lo, hi + 1):
        if arr[i] <= pivot:
            arr[i], arr[left_index] = arr[left_index], arr[i]
            left_index += 1

    quick_sort(arr, left_index - 2, lo)
    quick_sort(arr, hi, left_index)


arr = [int(i) for i in '9 8 6 7 3 5 4 1 2'.split()]
quick_sort(arr, len(arr) - 1, 0)
print(arr)

# def quick_sort(arr, hi, lo):
#     if lo >= hi or lo < 0:
#         return
#
#     pivot = arr[-1]
#     i = lo - 1
#     for j in range(lo, hi):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     i += 1
#     arr[i], arr[hi] = arr[hi], arr[i]
#
#     quick_sort(arr, i - 1, lo)
#     quick_sort(arr, hi, i + 1)
