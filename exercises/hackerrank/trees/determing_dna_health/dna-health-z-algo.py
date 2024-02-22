def z_algo(s):
    result = length = len(s)
    right = 0
    left = 0
    z = [length]

    for i in range(1, length):
        z.append(0)
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]

    return z


def z_search(text, pattern):
    concat = pattern + "$" + text
    l = len(concat)

    z = z_algo(concat)

    res = []
    for i in range(l):
        if z[i] == len(pattern):
            res.append(i - len(pattern) - 1)

    return res


genes = 'a b c aa d b'.split(' ')
health = list(map(int, ('1 2 3 4 5 6'.split(' '))))

print(genes)
print(health)
print()


def dna_health(genes, health, strand, first, last):
    genes_dict = {}
    genes = genes.split()
    health = list(map(int, health.split()))

    for i in range(len(genes)):
        if not genes_dict.get(genes[i]):
            genes_dict[genes[i]] = [health[i]]
        else:
            genes_dict[genes[i]].append(health[i])

    substrings = set(genes[first:last + 1])

    r = 0
    strand_health = 0
    for substring in substrings:
        r = z_search(strand, substring)

        for _ in range(len(r)):
            strand_health += sum(genes_dict[substring][:len(r) + 1])

    print(genes_dict)


dna_health(
    'a b c aa d b',
    '1 2 3 4 5 6',
    'caaab',
    1,
    5
)
