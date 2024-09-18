# Time Complexity O(n) | Space Complexity O(n)
def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    for c, r in zip(competitions, results):
        if r == 1:
            scores[c[0]] = scores.get(c[0], 0)+3
        else:
            scores[c[1]] = scores.get(c[1], 0)+3

    best_team = max(scores, key=lambda k: scores[k])
    print(scores)
    return best_team


if __name__ == "__main__":

    # Sample Input
    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 1, 1]

    ans = tournamentWinner(competitions, results)

    # Sample Output
    '''
    Java
    '''
    print(ans)
