# O(low*high*n) Time| O(low*high)

def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return CanMeasureInRange(measuringCups, low, high, memoization)


def CanMeasureInRange(measuringCups, low, high, memoization):
    memoizeKey = createHasableKey(low, high)

    if memoizeKey in memoization:
        return memoization[memoizeKey]

    if low < 0 and high < 0:
        return False

    canMeasure = False
    for cup in measuringCups:
        cupLow, cupHigh = cup

        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break

        canMeasure = CanMeasureInRange(
            measuringCups, low-cupLow, high-cupHigh, memoization)
        if canMeasure:
            break
        memoization[memoizeKey] = canMeasure
    return canMeasure


def createHasableKey(low, high):
    return f"{low}:{high}"


if __name__ == "__main__":
    cups = [[200, 210], [450, 465], [800, 850]]
    low = 2100
    high = 2300
    # expected = True

    ans = ambiguousMeasurements(cups, low, high)
    print(ans)
