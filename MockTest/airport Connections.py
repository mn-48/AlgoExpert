def airportConnections(AIRPORTS, routes, STARTING_AIRPORT):
    #  initial graph
    graph = { airport: [] for airport in AIRPORTS}

    for route in routes:
        if route[0] not in graph:
             graph[route[0]] = []
        graph[route[0]].append(route[1])
    # print(graph)

    visited = set()
    visite_airports(STARTING_AIRPORT, graph, visited)
    # print(visited)

    for airport in AIRPORTS:
        if airport not in visited:
            visite_airports(airport, graph, visited)
            visited.remove(airport)

    # print(visited)
    visited.add(STARTING_AIRPORT)
    return len(AIRPORTS) - len(visited)


def visite_airports(node, graph, visited):
    if node not in visited:
        visited.add(node)
        for next_node in graph[node]:
            visite_airports(next_node, graph, visited)





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