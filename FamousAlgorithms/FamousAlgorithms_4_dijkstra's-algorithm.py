import sys

# O(V+E) Time | O(V+E) Space
def dijkstrasAlgorithm(start, edges):

    Q, P = {start}, [sys.maxsize if i !=
                     start else 0 for i in range(len(edges))]

    # print(Q, P)
    while Q:
        n = Q.pop()
        # print(n)
        for e, d in edges[n]:
            if P[n] + d < P[e]:
                P[e] = min(P[e], P[n]+d)
                Q.add(e)

    return [-1 if a == sys.maxsize else a for a in P]


if __name__ == "__main__":

    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]

    ans = dijkstrasAlgorithm(start, edges)
    print(ans)
