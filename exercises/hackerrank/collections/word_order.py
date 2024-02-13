def word_order(l):
    s = {}
    for el in l:
        if el in s:
            s[el] += 1
        else:
            s[el] = 1

    print(len(s))
    print(" ".join([str(i) for i in s.values()]))


if __name__ == '__main__':
    t = int(input().strip())
    r = []
    for t_itr in range(t):
        r.append(input())

    word_order(r)
