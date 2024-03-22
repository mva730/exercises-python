class Solution:
    def nthUglyNumber(self, n: int) -> int:
        j = n
        i = n

        while j <= n:
            if self.is_ugly(i):
                print(i, j)
                j += 1

            i += 1

        return i - 1

    def is_ugly(self, n):
        base = n
        if n == 1:
            return True

        while n % 2 == 0:
            n = n // 2

        while n % 3 == 0:
            n = n // 3

        while n % 5 == 0:
            n = n // 5

        if n == 1:
            return True

        return False

    def generate_ugly(self, n):
        list1 = [0] * n
        list1[0] = 1

        a = b = c = 0
        for i in range(1, n):
            list1[i] = min(list1[a] * 2, list1[b] * 3, list1[c] * 5)
            if list1[a] * 2 == list1[i]:
                a += 1
            if list1[b] * 3 == list1[i]:
                b += 1
            if list1[c] * 5 == list1[i]:
                c += 1
        return list1[n - 1]


print(Solution().generate_ugly(10))
# print(Solution().nthUglyNumber(10))
