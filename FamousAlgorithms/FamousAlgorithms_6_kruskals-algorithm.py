

# # O(e*log(e)) Time and O(e+v) Space
# def kruskalsAlgorithm(edges):
#     edge_list = []

#     for v1, neighbors in enumerate(edges):
#         for v2, w  in neighbors:
#             if v1 < v2:
#                 edge_list.append([v1, v2, w])
#     sorted_edges = sorted(edge_list, key= lambda x: x[2])

#     unions = { v: [v] for v in range(len(edges))}
#     union_mappings = { v: v for v in range(len(edges))}
    
#     mst = [[] for _ in range(len(edges))]

#     for v1, v2, w in sorted_edges:
#         if union_mappings[v1] != union_mappings[v2]:
#             merge_unions(v1, v2, unions, union_mappings)
#             mst[v1].append([v2, w])
#             mst[v2].append([v1, w])
#     return mst

# def merge_unions(v1, v2, unions, union_mappings):
#     if len(unions[union_mappings[v1]]) >= len(unions[union_mappings[v2]]):
#         smaller_union = union_mappings[v2]
#         bigger_union = union_mappings[v1]
#     else:
#         smaller_union = union_mappings[v1]
#         bigger_union = union_mappings[v2]
#     for v in unions[smaller_union]:
#         union_mappings[v] = bigger_union
#         unions[bigger_union].append(v)
#     del unions[smaller_union]





# O(e*log(e)) Time and O(e+v) Space
def kruskalsAlgorithm(edges):
    edgeList = []

    for sourceIdx, vertex in enumerate(edges):
        for edge in vertex:
            if edge[0] > sourceIdx:
                edgeList.append([sourceIdx, edge[0], edge[1]])

    sortedEdges = sorted(edgeList, key=lambda edge: edge[2])

    parents = [vertex for vertex in range(len(edges))]
    ranks = [0 for _ in range(len(edges))]
    mst = [[] for _ in range(len(edges))]

    for edge in sortedEdges:
        vertex1Root = find(edge[0], parents)
        vertex2Root = find(edge[1], parents)

        if vertex1Root != vertex2Root:
            mst[edge[0]].append([edge[1], edge[2]])
            mst[edge[1]].append([edge[0], edge[2]])
            union(vertex1Root, vertex2Root, parents, ranks)
    return mst

def find(vertex, parents):
    if vertex != parents[vertex]:
        parents[vertex] = find(parents[vertex], parents)
    return parents[vertex]


def union(vertex1Root, vertex2Root, parents, ranks):
    if ranks[vertex1Root] < ranks[vertex2Root]:
        parents[vertex1Root] = vertex2Root
    elif ranks[vertex1Root] > ranks[vertex2Root]:
        parents[vertex2Root] = vertex1Root
    else:
        parents[vertex2Root] = vertex1Root
        ranks[vertex1Root] +=1

if __name__=="__main__":
    input = [[[1, 1]], [[0, 1]]]
    ans = kruskalsAlgorithm(input)
    print(ans)