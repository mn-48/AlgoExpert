# O(e * log(v)) Time | O(v+e) Space

import heapq

def primsAlgorithm(edges):
    # Initialize the min spanning tree, nodes visited and heap
    minSpanningTree = [[] for _ in edges]
    nodesVisited = set([0])
    minHeap = [(weight, 0, destination) for destination, weight in edges[0]]
    heapq.heapify(minHeap) 

    # Loop through graph and add n-1 edges (for loop for safety, no infinite loops)
    for _ in range(len(edges) - 1):
        # Pop off from the heap until unvisited node is popped
        nextNodeWeight, nextNodeOrigin, nextNodeDestination = heapq.heappop(minHeap)
        while nextNodeDestination in nodesVisited and minHeap:
            nextNodeWeight, nextNodeOrigin, nextNodeDestination = heapq.heappop(minHeap)

        # Add this new node to the nodes visited
        nodesVisited.add(nextNodeDestination)

        # Add the edge to the min spanning tree
        minSpanningTree[nextNodeOrigin].append([nextNodeDestination, nextNodeWeight])
        minSpanningTree[nextNodeDestination].append([nextNodeOrigin, nextNodeWeight])

        # Push all of these node's edges to the heap (only the unvisited ones)
        for nodeIdx, nodeWeight in edges[nextNodeDestination]:
            if nodeIdx in nodesVisited:
                continue
            heapq.heappush(minHeap, (nodeWeight, nextNodeDestination, nodeIdx))

    return minSpanningTree



if __name__=="__main__":
    input = [[[1, 1]], [[0, 1]]]
    ans =  primsAlgorithm(input)
    print(ans)