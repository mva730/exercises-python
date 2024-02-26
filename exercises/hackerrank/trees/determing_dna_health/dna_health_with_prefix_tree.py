import time

start_time = time.time()


class PrefixTree:

    def __init__(self, key):
        self.key = key
        self.children = {}
        self.data = {}

    def __repr__(self):
        return f"{self.children}"


def create_tree(genes, health):
    start_time = time.time()
    tree = PrefixTree('')

    for i in range(len(genes)):

        node = tree
        for char in genes[i]:
            if char not in node.children:
                node.children[char] = PrefixTree(char)
            node = node.children[char]

        node.data[i] = health[i]
    print("Tree build time --- %s seconds ---" % (time.time() - start_time))
    return tree


def get_health_sum(word, tree, first, last):
    health_sum = 0

    for i in range(len(word)):

        j = i
        node = tree
        while j < len(word) and word[j] in node.children:
            node = node.children[word[j]]
            if node.data:
                health_sum += get_sum_in_range(node.data, first, last)
                j += 1

    return health_sum


# def get_sum_in_range(data, first, last):
#     h = 0
#
#     for idx, health in data.items():
#         if first <= idx <= last:
#             h += health
#
#     return h


def get_sum_in_range(data, first, last):
    h = 0
    low_bound = 0
    l = 0
    data_list = list(data.items())
    r = len(data_list) - 1

    while l <= r:
        m = (l + r) >> 1

        if data_list[m][0] < first:
            l = m + 1
            low_bound = l
        else:
            r = m - 1
            low_bound = m

    while low_bound < len(data_list) and data_list[low_bound][0] <= last:
        h += data_list[low_bound][1]
        low_bound += 1

    return h


if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.read().splitlines()

    n = lines[0]
    genes = lines[1].rstrip().split()
    health = list(map(int, lines[2].rstrip().split()))
    t = create_tree(genes, health)
    s = int(lines[3].strip())
    r = []

    for s_itr in range(s):
        first_multiple_input = lines[4 + s_itr].rstrip().split()

        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]

        r.append(get_health_sum(d, t, first, last))

    print(min(r), max(r))

print("--- %s seconds ---" % (time.time() - start_time))
