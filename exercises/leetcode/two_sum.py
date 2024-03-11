def twoSum1(nums, target):
    d = {}
    for i, v in enumerate(nums):
        if d.get(v):
            d[v].append(i)
        else:
            d[v] = [i]

    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            if nums[i] == nums[j]:
                return [d[nums[i]][0], d[nums[j]][1]]
            return [d[nums[i]][0], d[nums[j]][0]]

        if nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1


def twoSum(nums, target):
    to_find = {}

    for i in range(len(nums)):
        value_to_find = target - nums[i]

        if value_to_find in to_find:
            return [to_find[value_to_find], i]

        to_find[nums[i]] = i

    return []


print(twoSum([7, 7, 2, 11, 15], 9))
