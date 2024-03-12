from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        rem = 1
        i = 0
        while rem and i + 1 <= len(digits):
            cur = digits[-1 - i]
            res = cur + 1

            if res > 9:
                rem = 1
            else:
                rem = 0

            digits[-1 - i] = res % 10
            i += 1

        if rem == 1:
            digits.insert(0, 1)

        return digits


print(Solution().plusOne([9]))
