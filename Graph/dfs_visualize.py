import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
# G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_nodes_from([1, 2, 3, 4, 5])



# Add edges

# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
G.add_edges_from([(1, 2), (1, 5), (2, 1), (2, 5), (2, 3), (2, 4),  (3, 2), (3, 4), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 4)])
# G.add_edges_from([(1, 2), (1, 5), (2, 1), (2, 5) (2, 4), (2, 3), (3, 2), (3, 5), (4, 5), (4, 2), (4, 3), (5, 1), (5,2), (5, 4)])

# DFS traversal function with visualization
def dfs_visualize(graph, start_node):
    visited = set()
    stack = [start_node]

    pos = nx.spring_layout(graph)
    plt.figure()

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            # Draw the graph at this step
            plt.clf()
            nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='black')
            nx.draw_networkx_nodes(graph, pos, nodelist=visited, node_color='green')
            plt.title(f'DFS Traversal - Visiting Node {current}')
            plt.pause(2)  # Pause to visualize the step

            # Push neighbors to the stack
            for neighbor in sorted(graph.neighbors(current), reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)

    plt.show()

# Run the DFS visualization
dfs_visualize(G, start_node=1)
