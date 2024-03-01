def crack(keys, password):
    stack = list()
    result = []
    visited = set()
    stack.append((password, result))

    while stack:
        p, result = stack.pop()
        if p in visited:
            continue

        visited.add(p)
        for key in keys:
            prefix = p[:len(key)]
            suffix = p[len(key):]

            if prefix == key:
                result.append(key)

                if len(suffix) == 0:
                    return result

                stack.append((suffix, result))

                result = result[:-1]

    return ['WRONG PASSWORD']


print(crack('a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa'.split(' '), 'aaaaaaaaaab'))
print(crack('we web adaman barcod'.split(' '), 'webadaman'))
