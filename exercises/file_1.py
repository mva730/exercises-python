# countries = dict()
# str_number = 0
# while (country := input()) != "X":
#     countries[country] = countries.get(country, []) + [str_number]
#     str_number += 1
#
# for country in countries:
#     print(f"{country}: {countries[country]}")
#
# matrix = [[int(x) for x in [1, 2, 3, 4, 5]] for i in range(5)]
# print(matrix)
#
# zeros = [[0] * 5] * 5
# print(zeros)
# zeros[0][0] = 1
# print(zeros)

# print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))
# print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3))

# s = '; '.join(str(x) for x in range(10 ** 7))
# print(s)

# n = 4
# x = [[x * i for x in range(1, n + 1)] for i in range(1, n + 1)]
# print(x)

# sentence = "1 222 3"
# print([len(x) for x in sentence.split()])

# numbers = [1, 2, 3, 4, 5]
# print({x for x in numbers if x % (x ** 0.5) == 0})
# string = "asdf aasdf"
# # print(string.split())
# print(''.join([x[0].upper() for x in string.split()]))

# numbers = [3, 1, 2, 3, 2, 2, 1]
# print(' - '.join([str(n) for n in sorted(set(numbers))]))

# rle = [('a', 2), ('b', 3), ('c', 1)]
# print([a * b for a, b in rle])
# print(''.join([a * b for a, b in rle]))

# numbers = {1, 2, 3, 4, 5}
# print({n: [x for x in range(1, n + 1) if n % x == 0] for n in numbers})

#
# text = '''Ехали медведи
# На велосипеде.
#
# А за ними кот
# Задом наперёд.'''
#
# print({x.lower(): text.lower().count(x.lower()) for x in text if x.isalpha()})
# {x: text.lower().count(x) for x in [letter.lower() for letter in text if letter.isalpha()]}

# squares = (i ** 2 for i in range(10))
# print(squares)


# def fib(n):
#     f_1, f = 1, 1
#     for i in range(n - 1):
#         # sum = f_1 + f
#         # f_1 = f
#         # f = sum
#         f, f_1 = f_1 + f, f
#     return f
#
#
# print(fib(5))

# def fib(n):
#     n_1, n_2 = 1, 1
#     for i in range(n):
#         yield n_1
#         n_1, n_2 = n_2, n_1 + n_2

# def recursive_sum(*args):
#     if len(args) == 1:
#         return args[0]
#
#     length = len(args) - 1
#
#     return args[length] + recursive_sum(*args[:length])
#
#
# print(recursive_sum(1, 2, 3))
# def recursive_digit_sum(n):
#     if n == 0:
#         return n
#
#     current = n % 10
#
#     return current + recursive_digit_sum(n // 10)


# print(recursive_digit_sum(1123))

# def make_equation(*args):
#     if len(args) == 1:
#         return f'{args[0]}'
#
#     length = len(args) - 1
#
#     return f'({make_equation(*args[:length])}) * x + {args[length]}'
#
#
# print(make_equation(3, 2, 1, 4))


def result_accumulator(f):
    result = []
    print(id(result))

    def dec(*args, method='accumulate'):
        nonlocal result
        print(id(result))
        result.append(f(*args))
        if method == 'drop':
            temp = result.copy()
            result.clear()
            return temp

    return dec


# @result_accumulator
# def a_plus_b(a, b):
#     return a + b
#
#
# print(a_plus_b(3, 5, method="accumulate"))
# print(a_plus_b(7, 9))
# print(a_plus_b(-3, 5, method="drop"))
# print(a_plus_b(1, -7))
# print(a_plus_b(10, 35, method="drop"))

@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))