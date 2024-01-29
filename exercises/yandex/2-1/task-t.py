n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

sum = n * m

# m1 = n - m2
# m1 * k1 + m2 * k2 = sum
# (n - m2) * k1 + m2 * k2 = sum
# n * k1 - m2 * k1 + m2 * k2 = sum
# m2 = (sum / (n * k1)) / (k2 - k1)
m2 = int((sum - (n * k1)) / (k2 - k1))
m1 = n - m2

print(m1, m2)
