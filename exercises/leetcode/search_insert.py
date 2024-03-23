class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)

        if target <= nums[l]:
            return l

        if target > nums[r - 1]:
            return r

        while l + 1 < r:
            m = l + r >> 1

            if nums[m] < target:
                l = m
            else:
                r = m

        return r


print(Solution().searchInsert([1, 2, 3, 4, 5], 2))
