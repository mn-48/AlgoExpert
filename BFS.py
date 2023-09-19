from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neibour in self.graph[vertex]:
                if neibour not in visited:
                    visited.add(neibour)
                    queue.append(neibour)

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("Breadth-First Traversal (starting from vertex 2):")

g.bfs(2)