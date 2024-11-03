# import math


# def detectArbitrage(exchangeRates):
#     logExchangeRates = convertToLogMatrix(exchangeRates)
#     # print(exchangeRates)
#     # print()
#     # print(logExchangeRates)

#     return foundNegativeWeightCycle(logExchangeRates, 0)

# def foundNegativeWeightCycle(graph, start):
#     distanceFromStart = [float('inf') for _ in range(len(graph))]
#     distanceFromStart[start] = 0

#     for _ in range(len(graph)-1):
#         if not relaxEdgesAndUpdateDistances(graph, distanceFromStart):
#             return False
#     return relaxEdgesAndUpdateDistances(graph, distanceFromStart)


# def relaxEdgesAndUpdateDistances(graph, distances):
#     update = False
#     for sourceIdx, edges in enumerate(graph):
#         for destinationIdx, edgeWeight in enumerate(edges):
#             newDistanceToDestination = distances[sourceIdx] + edgeWeight
#             if newDistanceToDestination < distances[destinationIdx]:
#                 update = True
#                 distances[destinationIdx] = newDistanceToDestination

#     return update

# def convertToLogMatrix(matrix):
#     newMatrix = []
#     for row, rates in enumerate(matrix):
#         newMatrix.append([])
#         for rate in rates:
#             newMatrix[row].append(-math.log10(rate))
#     return newMatrix



# O(n^3) Time | O(n) Space


def detectArbitrage(exchangeRates):
    n = len(exchangeRates)
    d = [float('-inf')]*n

    d[0] = 1
    for _ in range(n):
        x = -1
        for p in range(n):
            for q in range(n):
                cand_exchange = d[p] * exchangeRates[p][q]
                if cand_exchange > d[q]:
                    d[q] = cand_exchange
                    x = p
    return x != -1
    
    # Write your code here.
    return False











if __name__=="__main__":
    input = [[1.0, 0.8631, 0.5903], [1.1586, 1.0, 0.6849], [1.6939, 1.46, 1.0]]
    ans =detectArbitrage(input)
    print(ans)