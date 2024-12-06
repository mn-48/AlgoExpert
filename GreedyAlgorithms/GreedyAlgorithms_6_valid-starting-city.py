# O(n) Time | O(1) Space

def validStartingCity(distances, fuel, mpg):
    biggestNegative = 0
    bestStartIndex = 0

    currSum = 0
    for i in range(len(distances)):
        currSum += fuel[i] * mpg - distances[i]

        if currSum < biggestNegative:
            biggestNegative = currSum
            bestStartIndex = (i+1) % len(distances)
    return bestStartIndex

if __name__=="__main__":
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    ans =  validStartingCity(distances, fuel, mpg)
    print(ans)