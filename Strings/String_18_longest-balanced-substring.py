# O(n) Time | O(1) Space

def longestBalancedSubstring(string):
    maxLength = 0
    openingCount = 0
    closingCount = 0

    for char in string:
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1
        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0

    openingCount = 0
    closingCount = 0

    for i in reversed(range(len(string))):
        char = string[i]
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)

        elif closingCount < openingCount:
            openingCount = 0
            closingCount = 0
    return maxLength
