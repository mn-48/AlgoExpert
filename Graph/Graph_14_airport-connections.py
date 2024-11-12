# O(a+r) time/space, 40 lines, random node review (whaaat???)

# shared by andrii.kusch on September 1, 2023

# Explanation
# Consider a tree. If you picking nodes at random and eliminating the node and all of its children. Regardless of the order and how long it takes, your last node to eliminate will be the tree's root as it is cannot be reached from other nodes.

# Now extend this logic to a graph. If in a graph you randomly pick a node and eliminate it and all nodes reachable from it, the last nodes standing will be nodes you cannot reach from other nodes, sort of "roots" or lets call them entries.

# The question asks you to find a minimum connections to add to make the graph fully connected from the starting airport. That means that you need to connect the start nodes to all the entries of subgraph of unreachable airports.

# So the algorithm is:
# 1) Find all airports not reachable from the starting airport
# 2) In any order pick one, remove it and all airports reachable from it
# 3) Repeat keeping track of the order you picked them in in an array. This array will have a useful property: for every node everything that is to the right from it (that was added later to the array) is not reachable from the node. And right-most is guaranteed to be an entry (one of the last standing nodes unreachable from others)
# 4) in reversed order, right to left, pick entries and remove everything reachable from them from the list.
# In the end you will have all the entries: nodes that are not reachable from any other nodes, so they have to be connected to the starting airport to make the entire graph fully connected, which is what the question is asking for

# import random

# #  O(a+r) Time | O(a+r) Space
# def airportConnections(airports, routes, startingAirport):

#     # adjacency list O(r+a) Time/Space
#     graph = {}
#     for from_ , to_ in routes:
#         if from_ not in graph:
#             graph[from_] = []
#         graph[from_].append(to_)

#     for airport in airports:
#         if airport not in graph:
#             graph[airport] = []
    
#     # get airports reachable from entry O(a+r) time/space
#     def reachableFrom(node, visited):
#         if node in visited:
#             return
#         visited.add(node)
#         for neighbor in graph[node]:
#             reachableFrom(neighbor, visited)
#         return visited
    
#     reachableFromStart = reachableFrom(startingAirport,visited=set()) # O(a+r) time & space
#     unreachableFromStart = set(airports)- reachableFromStart # O(n)

#     # MAGIC!!! O(a+r) time/Space

#     potentialEntries = []
#     while len(unreachableFromStart) > 0:
#         # Order in which you review unreachable nodes is irrelevant
#         # could as well be random, which I show here. otherwise just do
#         # potentialEntry = unreachableFromStart.pop()
#         potentialEntry = random.sample(unreachableFromStart, 1)[0]
#         potentialEntries.append(potentialEntry)
#         unreachableFromStart -= reachableFrom(potentialEntry, visited=set())

#     connectionsToAdd = 0
#     while len(potentialEntries) > 0:
#         connectionsToAdd += 1
#         entry = potentialEntries.pop()
#         reachableFromEntry = reachableFrom(entry, visited=set())
#         potentialEntries = [airport for airport in potentialEntries if airport not in reachableFromEntry]

#     return connectionsToAdd
         

# O(a+r) Time | O(a+r) Space
def airportConnections(airports, routes, startingAirport):
    graph = { airport: [] for airport in airports }
    for src, dest in routes:
        graph[src].append(dest)

    visited = set()
    visitAirports(startingAirport, graph, visited)

    for airport in airports:
        if airport not in visited:
            visitAirports(airport, graph, visited)
            visited.remove(airport) # remove it

    visited.add(startingAirport)
    return len(airports) - len(visited)

def visitAirports(node, graph, visited):
    if node not in visited:
        visited.add(node)
        for nextNode in graph[node]:
            visitAirports(nextNode, graph, visited)

     





if __name__=="__main__":
    AIRPORTS = [
        "BGI",
        "CDG",
        "DEL",
        "DOH",
        "DSM",
        "EWR",
        "EYW",
        "HND",
        "ICN",
        "JFK",
        "LGA",
        "LHR",
        "ORD",
        "SAN",
        "SFO",
        "SIN",
        "TLV",
        "BUD",
    ]

    routes = [
        ["DSM", "ORD"],
        ["ORD", "BGI"],
        ["BGI", "LGA"],
        ["SIN", "CDG"],
        ["CDG", "SIN"],
        ["CDG", "BUD"],
        ["DEL", "DOH"],
        ["DEL", "CDG"],
        ["TLV", "DEL"],
        ["EWR", "HND"],
        ["HND", "ICN"],
        ["HND", "JFK"],
        ["ICN", "JFK"],
        ["JFK", "LGA"],
        ["EYW", "LHR"],
        ["LHR", "SFO"],
        ["SFO", "SAN"],
        ["SFO", "DSM"],
        ["SAN", "EYW"],
    ]

    STARTING_AIRPORT = "LGA"

    ans = airportConnections(AIRPORTS, routes, STARTING_AIRPORT) 
    print(ans)