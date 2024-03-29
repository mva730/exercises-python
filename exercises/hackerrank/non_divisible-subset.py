# def nonDivisibleSubset(s, k):
#     length = len(s)
#     res = set()
#     for i in range(length - 1, -1, -1):
#         perms = permutations(s, i)
#
#         for perm in perms:
#             subs = permutations(perm, 2)
#
#             result = True
#             for sub in subs:
#                 if sum(sub) % k != 0:
#                     result = False
#                     break
#             if result:
#                 res.add(len(perm))
#
#     return max(res)
from itertools import permutations


# def nonDivisibleSubset(s, k):
#     goods = set()
#     bads = set()
#
#     perms = permutations(s, 2)
#     for perm in perms:
#         if sum(perm) % k != 0:
#             goods.add(perm)
#         else:
#             bads.add(perm)
#
#     b = set(sum(map(list, bads), []))
#
#     return len(b)

#  https://www.hackerrank.com/challenges/non-divisible-subset/forum

# This initially appears difficult to solve in reasonable time complexity. After further thought, I think this can be done on O(n) with a few considerations. This is supposed to be an "easy" problem, so I'll provide some algorithm guidance here.
#
# For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K. (There is also a special case where both A & B are evenly divisible, giving a sum of 0.)
#
# For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K.
#
# Example: with K of 5, remainder pairs are 1+4 & 2+3. Given the numbers with a remainder of 1, they can't be paired with ANY of the numbers with remainder 4 (and vice versa). So, for the number of values in the resultant set, choose the larger of values with remainder 1 vs. values with remainder 4. Choose the larger set of remainder 2 vs remainder 3.
#
# For the special case where remainder is 0, given the set of all values which are individually divisible by K, they can't be paired with any others. So, at most 1 value which is evenly divisible by K can be added to the result set.
#
# For even values of K, the equal remainder is simular to the 0 case. For K = 6, pairs are 1+5, 2+4, 3+3. For values with remainder 3, at most one value can be added to the result set.

def nonDivisibleSubset(numbers, k):
    counts = [0] * k
    for number in numbers:
        print(number, number % k)
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            print(i, k - i)
            print(counts[i], counts[k - i])
            count += max(counts[i], counts[k - i])

    if k % 2 == 0 and counts[k // 2] > 0:
        count += 1

    print(count)


print(nonDivisibleSubset(list(map(int, '1 5 8'.split())), 6))
perms = permutations(list(map(int, '1 5 8'.split())), 2)
print(list(perms))
