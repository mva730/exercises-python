class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = []
        left = x

        while left:
            numbers.append(left % 10)
            left = left // 10

        print(numbers)

        i = 0
        j = len(numbers) - 1

        while i <= j:
            if numbers[i] != numbers[j]:
                return False
            i += 1
            j -= 1

        return True


Solution().isPalindrome(12121)
