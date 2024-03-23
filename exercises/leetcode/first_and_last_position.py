class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        l = -1
        r = len(nums)

        res = []
        while l + 1 < r:
            m = l + r >> 1

            if nums[m] < target:
                l = m
            else:
                r = m

        res.append(r)

        l = -1
        r = len(nums)
        while l + 1 < r:
            m = l + r >> 1

            if nums[m] <= target:
                l = m
            else:
                r = m

        res.append(l)

        if res[0] < len(nums) and res[1] < len(nums):
            if nums[res[0]] == target or nums[res[1]] == target:
                return res

        return [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
