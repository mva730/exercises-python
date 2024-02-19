def climbing_leaderboard_binary_search(ranked, player):
    rank = 0
    dict = {}
    for score in ranked:
        if not dict.get(score):
            rank += 1
            dict[score] = rank

    for score in player:
        l = 0
        r = len(ranked)

        while r - l > 1:
            m = (l + r) // 2

            if score > ranked[m]:
                r = m
            else:  # score <= ranked[m]
                l = m

            print(l, r)

        if score < ranked[l]:
            print(dict[ranked[l]] + 1)
        else:
            print(dict[ranked[l]])


def climbing_leaderboard(ranked, player):
    rank = 0
    dict = {}

    for score in ranked:
        if not dict.get(score):
            rank += 1
            dict[score] = rank

    for player_score in player:
        for i in range(len(ranked)):
            if player_score >= ranked[i]:
                print(dict[ranked[i]])
                break
            if len(ranked) - i == 1:
                print(dict[ranked[i]] + 1)


# [l, r)
# climbing_leaderboard_binary_search([int(i) for i in "100 100 50 40 40 20 10".split()],
#                                    [int(i) for i in "5 25 50 120".split()])
#                                                     0   1  2  3
climbing_leaderboard_binary_search([int(i) for i in "100 100 50 40 40 20 10".split()],
                                   [int(i) for i in "5 25 50 120".split()])
