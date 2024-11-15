# O(n^2) Time | O(n^2) Space

def stableInternships(interns, teams):
    # print(interns, teams)
    choosenInterns = {}
    freeInterns = list(range(len(interns)))
    # print(freeInterns)
    currentInternChoices = [0]*len(interns)
    # print(currentInternChoices)

    teamMaps = []
    
    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)
    # print(teamMaps)

    while len(freeInterns) > 0:
        internNum = freeInterns.pop()
        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]

        currentInternChoices[internNum] +=1

        if teamPreference not in choosenInterns:
            choosenInterns[teamPreference] = internNum
            continue

        previousIntern = choosenInterns[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNum]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            choosenInterns[teamPreference] = internNum
        else:
            freeInterns.append(internNum)

    matches = [[internNum, teamNum] for teamNum, internNum in choosenInterns.items()]
    return matches        


if __name__=="__main__":
    interns = [[0, 1], [1, 0]]
    teams = [[1, 0], [1, 0]]
    ans = stableInternships(interns, teams)
    print(ans)