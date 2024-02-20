def isValid1(s):
    dict = {}
    max_val = 0
    for c in s:
        if not dict.get(c):
            dict[c] = 1
        else:
            dict[c] += 1
            if dict[c] > max_val:
                max_val = dict[c]

    if len(set(dict.values())) == 1:
        return print('YES')

    if len(set(dict.values())) > 2:
        return print('NO')

    if len(set(dict.values())) == 2:
        values = list(set(dict.values()))

        if abs(values[1] - values[0]) > 1:
            return print('NO')

        max_val_values_num = [(k, v) for k, v in dict.items() if v == max_val]

        if len(max_val_values_num) == 1 or len(max_val_values_num) == len(dict) - 1:
            return print('YES')

    return print('NO')


isValid1('aabbccddeefghi')
