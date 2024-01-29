results_dict = {0: 1, 1: 1}


def cached_fib(n):
    if n in results_dict:
        return results_dict[n]

    result = cached_fib(n - 1) + cached_fib(n - 2)
    results_dict[n] = result

    return result


cached_fib(100)
for v in results_dict.values():
    print(v)
