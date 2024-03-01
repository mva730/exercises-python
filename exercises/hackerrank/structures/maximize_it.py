import itertools


def maximize_it(lsts, M):
    # print(r)

    res = []
    for combo in itertools.product(*lsts):

        s = 0
        for i in combo:
            s += i ** 2

        res.append(s % M)

    return max(res)


if __name__ == '__main__':
    t = input().strip().split()
    t_itr = t[0]
    M = t[1]
    r = []
    for _ in range(int(t_itr)):
        r.append([int(i) for i in input().strip().split()[1:]])

    print(maximize_it(r, int(M)))
