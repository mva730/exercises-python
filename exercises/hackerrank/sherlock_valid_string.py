# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

def isValid(s):
    dict = {}
    max_val = 0
    for c in s:
        if not dict.get(c):
            dict[c] = 1
        else:
            dict[c] += 1
            if dict[c] > max_val:
                max_val = dict[c]

    values_set = set(dict.values())

    if len(values_set) == 1:
        return print('YES')

    if len(values_set) > 2:
        return print('NO')

    if len(values_set) == 2:

        values = list(values_set)

        if abs(values[1] - values[0]) > 1:
            if values.count(1) == 0 or list(dict.values()).count(1) > 1:
                return print('NO')

        max_val_values_num = [(k, v) for k, v in dict.items() if v == max_val]

        # last_value = [i for i in values if values != max_val][0]
        if len(max_val_values_num) == 1 or (len(max_val_values_num) == len(dict) - 1 and sorted(values)[0] == 1):
            return print('YES')

    return print('NO')


isValid('aaabbbcc')
