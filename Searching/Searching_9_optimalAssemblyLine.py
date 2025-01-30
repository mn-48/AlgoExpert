# O(n*log(m)) time | O(1) space
def optimalAssemblyLine(stepDurations, numStations):
    left, right = max(stepDurations), sum(stepDurations)
    maxStationDuration = float("inf")
    while left <= right:
        potentialMaxStationDuration = (left + right) // 2
        if isPotentialSolution(stepDurations, numStations, potentialMaxStationDuration):
            maxStationDuration = potentialMaxStationDuration
            right = potentialMaxStationDuration - 1
        else:
            left = potentialMaxStationDuration + 1
    return maxStationDuration


def isPotentialSolution(stepDurations, numStations, potentialMaxStationDuration):
    stationRequired = 1
    currentDuration = 0

    for stepDuration in stepDurations:
        if currentDuration + stepDuration > potentialMaxStationDuration:
            stationRequired += 1
            currentDuration = stepDuration
        else:
            currentDuration += stepDuration
    return stationRequired <= numStations


if __name__=="__main__":
    stepDurations = [15, 15, 30, 30, 45]
    numStations = 3
    ans = optimalAssemblyLine(stepDurations, numStations)
    print(ans)