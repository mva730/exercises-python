import itertools


def threeSum(nums):
    nums = set(nums)

    combs = set(itertools.combinations(nums, 2))

    result = set()
    for comb in combs:
        for num in nums:
            if sum(comb) + num == 0:
                l = list(comb)
                l.append(num)
                result.add(tuple(sorted(l)))

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
