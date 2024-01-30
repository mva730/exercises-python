# n = input()
# ar = [int(i) for i in input().split()]

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    left = []
    right = []
    pivot = arr[0]
    for el in arr[1:]:
        if el > pivot:
            right.append(el)
        else:
            left.append(el)

    left = quick_sort(left)
    right = quick_sort(right)
    print(1)
    print(' '.join([str(i) for i in left + [pivot] + right]))
    return left + [pivot] + right


quick_sort([5, 8, 1, 3, 7, 9, 2])
