from math import inf


def threeSumClosest(nums, target):
    nums.sort()

    res = inf
    for i in range(len(nums)):

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            potentialSum = nums[i] + nums[l] + nums[r]
            if potentialSum == target:
                return potentialSum

            if potentialSum > target:
                # last_third = nums[r]
                # while l < r and last_third == nums[r]:
                r -= 1
            else:
                # last_second = nums[l]
                # while l < r and last_second == nums[l]:
                l += 1

            if abs(potentialSum - target) < abs(res - target):
                res = potentialSum

    return res


print(threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
