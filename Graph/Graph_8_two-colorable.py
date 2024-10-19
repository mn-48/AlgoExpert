
# O(V+E) Time | O(V) Space
 
def twoColorable(edges):
    colors = [None] * len(edges)
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()

        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False
                        
    # Write your code here.
    return True
