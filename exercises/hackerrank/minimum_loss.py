# def minimum_loss(price):
#     sorted_arr = sorted(price)[::-1]
#
#     minimums = set()
#     for i in price:
#         to_find = -1
#         for number in range(i, -1, -1):
#             l = 0
#             r = len(sorted_arr)
#
#             while l + 1 < r:
#                 m = (l + r) // 2
#
#                 if number == sorted_arr[m]:
#                     to_find = number
#                     break
#                 if number > sorted_arr[m]:
#                     l = m
#                 else:
#                     r = m
#
#             if to_find != -1:
#                 if price.index(to_find) > price.index(i):
#                     minimums.add(i - number)
#                     break
#
#     return min(minimums)


def minimum_loss2(prices):
    sorted_arr = sorted(prices)[::-1]

    minimums = set()
    for price in prices:
        current_price_sorted_index = sorted_arr.index(price)

        for i in range(current_price_sorted_index, len(sorted_arr)):
            if prices.index(price) < prices.index(sorted_arr[i]):
                # 20 8 7 5 2
                minimums.add(price - sorted_arr[i])
                break

    return min(minimums)


def minimum_loss3(prices):
    sorted_arr = sorted([(p, i) for i, p in enumerate(prices)])

    i = 0
    j = 1

    minimum = 10e17
    while j < len(sorted_arr):
        if sorted_arr[j][1] < sorted_arr[i][1] and sorted_arr[j][0] - sorted_arr[i][0] < minimum:
            minimum = sorted_arr[j][0] - sorted_arr[i][0]

        i += 1
        j += 1

    return minimum


def minimum_loss4(prices):
    sorted_arr = sorted(prices)

    i = 0
    j = 1

    minimum = 10e17
    while j < len(sorted_arr):
        if prices.index(sorted_arr[j]) < prices.index(sorted_arr[i]) and sorted_arr[j] - sorted_arr[i] < minimum:
            minimum = sorted_arr[j] - sorted_arr[i]

        i += 1
        j += 1

    return minimum


def minimum_loss(price):
    # Write your code here
    priceS = sorted([(p, i) for i, p in enumerate(price)])
    return min([priceS[i + 1][0] - priceS[i][0] for i in range(len(priceS) - 1) if priceS[i + 1][1] < priceS[i][1]])


print(minimum_loss3([int(i) for i in "20 7 8 2 5".split()]))
