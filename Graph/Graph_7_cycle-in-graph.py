# O(V+E) Time| O(V) Space

# def cycleInGraph(edges):
#     # Write your code here.
#     numberOfNodes = len(edges)

#     visited = [False] * numberOfNodes
#     stack = [False] * numberOfNodes

#     for node in range(numberOfNodes):

#         if visited[node]:
#             continue
#         containCycle = isNodeInCycle(edges, node, visited, stack)

#         if containCycle:
#             return True

#     return False

# def isNodeInCycle(edges, node, visited, stack):
#     visited[node] = True

#     stack[node] = True

#     neighbors = edges[node]

#     for neighbor in neighbors:
#         if not visited[neighbor]:
#             containCycle = isNodeInCycle(edges, neighbor, visited, stack)
#             if containCycle:
#                 return True
#         elif stack[neighbor]:
#             return True

#     stack[node] = False
#     return False


# O(V+E) Time| O(V) Space

WHITE, GREY, BLACK = 0, 1, 2


def cycleInGraph(edges):
    numberOfNodes = len(edges)
    colors = [WHITE] * numberOfNodes

    for node in range(numberOfNodes):
        if colors[node] != WHITE:
            continue

        containCycle = traverseAndColorNodes(node, edges, colors)
        if containCycle:
            return True
    return False




def traverseAndColorNodes(node, edges, colors):
    colors[node] = GREY
    
    neighbors = edges[node]

    for neighbor in neighbors:
        neighbor_color = colors[neighbor]

        if neighbor_color == GREY:
            return True
        if neighbor_color != WHITE:
            continue
        containCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containCycle:
            return True
    colors[node] = WHITE

    return False

     
     
     
      
    
    
    
      
if __name__=="__main__":
    
    input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    ans = cycleInGraph(input)
    print(ans)