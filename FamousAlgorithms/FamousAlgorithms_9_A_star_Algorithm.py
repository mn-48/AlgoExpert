'''
O(m*n) algorithm

Explanation
------------

Forget about A* Algorithm, I have an O(m*n) algorithm, which also guarantees the shortest path length.

Time and space complicity depends on the elements pushed into queue which at most k, (k is the number of 0s in the graph, each 0 only will be visit once). k has upper limit of the graph size m*n

Note, please conder following factors if you think it is slower
(1)  queue implementation is list and can be replaced by double-end queue to achieve O(1) for pop()
(2) path can be obtained in O(p) time (p is the path length, which have upper boundary m*n) and O(m*n) space: create a same size map, where each cell restores where the explorer came from. Reverse construct path from the distination cell after path finding.
'''
from collections import deque


def neighbors(x, y, m, n):
    for (dx, dy) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= x+dx < m and 0 <= y+dy < n:
            yield (x+dx, y+dy)


def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    dq = deque()
    dq.append((startRow, startCol, [[startRow, startCol]]))
    while dq:
        (x, y, path) = dq.popleft()
        if x==endRow and y==endCol:
            return path
        for (x, y) in neighbors(x, y, len(graph), len(graph[0])):
            if graph[x][y] == 0:
                graph[x][y] = 1
                dq.append((x, y, path + [[x, y]]))
    return []
