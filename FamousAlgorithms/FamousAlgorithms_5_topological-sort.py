# O(J+D) Time | O(J+D) Space

from collections import defaultdict 
class GraphNode:
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

def topologicalSort(jobs, deps):
    graph = defaultdict(GraphNode)
    totalDeps = 0

    # Create an adjancency matrix marking amount of nodes comming 
    # in and the nodes leading out 
    for k, v in deps:
        # We keep track of total dependencies so that we can be
        # sure that we hit all the jobs in the end 
        totalDeps += 1
        graph[k].outNodes.append(v)
        graph[v].inDegrees += 1

    result = []

    # If the job is standalone, we can immediately add it to the result

    for job in jobs:
        if job not in graph:
            result.append(job)
    
    #  Create a queue for storing all nodes with zero incomming nodes
    q = []

    for k, v in graph.items():
        if v.inDegrees == 0:
            q.append(k)
    
    depsSeen = 0

    while q:
        node = q.pop(0)
        result.append(node)

        for neighbor in graph[node].outNodes:
            # print(neighbor)
            depsSeen += 1 
            graph[neighbor].inDegrees -= 1
            if graph[neighbor].inDegrees == 0:
                q.append(neighbor)
    # print(depsSeen, totalDeps)
    return result if depsSeen == totalDeps else []


if __name__=="__main__":
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    ans = topologicalSort(jobs, deps)
    print(ans)
