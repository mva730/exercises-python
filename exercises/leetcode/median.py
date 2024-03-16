from typing import List


class Solution:
    def findMedianSortedArrays(self, left: List[int], right: List[int]):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1

        if len(res) % 2 == 0:
            lres = res[len(res) // 2 - 1]
            rres = res[len(res) // 2]
            return (lres + rres) / 2

        return res[len(res) // 2]


print(Solution().findMedianSortedArrays([1, 2], [1, 2, 2]))
