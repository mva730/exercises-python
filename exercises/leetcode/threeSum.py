def threeSum(nums):
    nums.sort()
    triplets = set()

    for i in range(len(nums)):

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            potentialSum = nums[i] + nums[l] + nums[r]
            if potentialSum > 0:
                r -= 1
            elif potentialSum < 0:
                l += 1
            else:
                triplets.add((nums[i], nums[l], nums[r]))
                last_second = nums[l]
                last_third = nums[r]

                while l < r and last_second == nums[l]:
                    l += 1
                while l < r and last_third == nums[r]:
                    r -= 1
    return triplets


def threeSum_firstAttempt(nums):
    r = {}
    for i in range(len(nums)):
        to_find = set()
        target = nums[i]

        for j in range(i + 1, len(nums)):

            # target + value_to_find + nums[i] = 0
            # value_to_find = -nums[i] - target
            value_to_find = - target - nums[j]

            if value_to_find in to_find:
                l = [target, value_to_find, nums[j]]
                fr = frozenset(l)
                r[fr] = l

            to_find.add(nums[j])

    return list(r.values())


print(threeSum([-1, 0, 1, 2, -1, -4]))
