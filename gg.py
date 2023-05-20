def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    max_score = 0
    best_team = ""
    for c, r in zip(competitions, results):
        # print(c, r)
        if r==1:
            scores[c[0]] = scores.get(c[0], 0)+3

            # best_team = c[0]
            # scores[c[0]] = scores.get(c[0], 0)+3
            # if max_score < scores[c[0]]:
            #     max_score = scores[c[0]]
            #     best_team = c[0]
        else:
            scores[c[1]] = scores.get(c[1], 0)+3
            # best_team = c[1]
            # scores[c[1]] = scores.get(c[1], 0)+3
            # if max_score+3 < scores[c[1]]:
            #     max_score = scores[c[1]]
            #     best_team = c[1]
    # print(best_team)
    print('scores: ', scores)
    best_team = max(scores, key=lambda k: scores[k])
    print(best_team)
    return best_team

# competitions = [
#   ["HTML", "C#"],
#   ["C#", "Python"],
#   ["Python", "HTML"]
# ]

# results = [0, 0, 1]

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]

results = [0, 1, 1]


tournamentWinner(competitions, results)