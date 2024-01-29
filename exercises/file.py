# lo = [x if x % 2 == 0 else None for x in range(100)]
# lo.reverse();
#
# while len(lo) > 0:
#     print(lo.pop())
#     print(len(lo))

# from itertools import repeat
# from itertools import *
#
# X = []
# X.extend(list(map(int, input().split())))
# X.extend(list(map(int, input().split())))
# X.extend(list(map(int, input().split())))
#
# Ans = 72
# for P in permutations(range(1, 10)):
#     if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[
#         8] == 15 and (P[2] + P[4] + P[6] == 15):
#         Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0, 9)))
# print(Ans)

# print(list(zip("ABCDE", [1, 2, 3])))

# import json
#
# with open("f.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)
# records[1]["group_number"] = "asd"
# with open("data.json", "w", encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent=2)

#
# def add_value(x, y=[]):
#     y += [x]
#     return y
#
#
# print(add_value(1))
# print(add_value(1))
# print(add_value(1))
#
# def final_price(price, discount=1):
#     return price - price * discount / 100
#
#
# print(final_price(discount=5))
# print(final_price(discount=10, price=1000))

# def square(x):
#     return x ** 2


# list1 = [12, 3, 4, 15]
# s = 0
# for a in list1:
#     s += a
# print(s)

# from timeit import timeit
#
#
# def fib(n):
#     if n not in cash:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# cash = {1: 1, 0: 1}
#
# print(f"Среднее время вычисления: "
#       f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} с.")
# total = 0
#
#
# # Декоратор принимает функцию f как аргумент
# def count(f):
#     # Объявляем функцию, которая расширяет функционал f
#     def decorated(*args, **kwargs):
#         # Переменная total объявлена нелокальной для доступа из внутренней функции
#         global total
#         total += 1
#         # Возвращаем значение исходной функции и дополнительно total
#         return f(*args, **kwargs), total
#
#     # Возвращаем новую функцию как объект
#     return decorated
#
#
# @count
# def hello(name):
#     return f"Привет, {name}!"
#
#
# print(hello("Пользователь_1"))
# print(hello("Пользователь_2"))

# class A:
#
#     def __init__(self):
#         self.value = 101
#
#     def __add__(self, other):
#         self.value + other
#         # return self.value

#
# return "Выполняется метод __add__."

#     def __radd__(self, other):
#         return "Выполняется метод __radd__."
#
#     def __iadd__(self, other):
#         self.value += other
#         return self
#
#     def __str__(self):
#         return f"value: {self.value}."
#
#     def get_value(self):
#         return self.value
#
#
# a = A()
# print(a + 1)
# print(1 + a)
#
# # print(a)
# a += 1
# print(a.get_value())

# import math

# abcd
# ab
# cd
# ac
# ad
# bc
# bd

# print(math.comb(4, 3))
# print(math.perm(3, 2))
# print(2.72 ** 0.69)
# print(math.log(10, 2))
# print(math.log(2))

counter = 0


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     print(a[:n // 2])
#     print(a[n // 2:])
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:])
#
#     print(f"Left: {l}")
#     print(f"Right: {r}")
#
#     i = j = 0
#     res = []
#     while i < len(l) and j < len(r):
#         if l[i] <= r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     while i < len(l):
#         res.append(l[i])
#         i += 1
#     while j < len(r):
#         res.append(r[j])
#         j += 1
#
#     print(res)
#     return res
#
#
# print(merge_sort([1, 2, 4, 3, 3, 2]))
#
#
# def same_name(f):
#     def decorated(*args):
#         current_type = type(args[0])
#         for arg in args[1:]:
#             if type(arg) is not current_type:
#                 print("Обнаружены различные типы данных")
#                 return
#             current_type = type(arg)
#         return f(*args)
#
#     return decorated
#
#
# @same_name
# def combine_text(*words):
#     return ' '.join(words)
#
#
# print(combine_text('Hello,', 'world!') or 'Fail')
# print(combine_text(2, '+', 2, '=', 4) or 'Fail')
# print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
#
# print([1, 2, 3][0:3])

# def fib(n):
#     n_0 = 0
#     n_1 = 1
#
#     for i in range(0, n):
#         yield n_0
#         n_0, n_1 = n_1, n_0 + n_1
#
#
# print(fib(4))

def cust_cycle(arr):
    while arr:
        for i in range(0, 3):
            yield arr[i]


#
# def c(a):
#     while a:
#         yield print(a)

print(list(zip(range(5), cust_cycle([1, 2, 3]))))
print("abc"[::-1])
# def make_linear(a):
#     if not isinstance(a, list):
#         return a
#     cont = []
#     for i in range(0, len(a)):
#         result = make_linear(a[i])
#
#         if type(result) is int:
#             print(result)
#             cont.append(result)
#         else:
#             print(result)
#             cont.extend(result)
#     return cont
#
#
# def make_linear_2(arr):
#     new_arr = []
#     for i in arr:
#         if isinstance(i, list):
#             print(i)
#             new_arr.extend(make_linear(i))
#         else:
#             print(i)
#             new_arr.append(i)
#     return new_arr


# def make_linear(arr):
#     container = []
#
#     def scroll(brr):
#         if not isinstance(brr, list):
#             container.append(brr)
#             return brr
#         for i in range(0, len(brr)):
#             scroll(brr[i])
#
#     scroll(arr)
#
#     return container


# print(make_linear([1, [2, [3, 4]], 5, 6]))
# print(make_linear_2([1, [2, [3, 4]], 5, 6]))
