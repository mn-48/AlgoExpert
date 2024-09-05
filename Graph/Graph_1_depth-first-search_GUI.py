import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array, G, pos, ax):
        array.append(self.name)
        # Update visualization
        self._draw_graph(G, pos, ax, visited_nodes=array)
        plt.pause(1)  # Pause to visualize the DFS step

        for child in self.children:
            if child.name not in array:
                child.depthFirstSearch(array, G, pos, ax)

        return array

    def to_networkx_graph(self):
        G = nx.DiGraph()
        self._add_edges_to_graph(G)
        return G

    def _add_edges_to_graph(self, graph):
        for child in self.children:
            graph.add_edge(self.name, child.name)
            child._add_edges_to_graph(graph)

    def _draw_graph(self, G, pos, ax, visited_nodes):
        ax.clear()
        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='black', font_size=10, font_weight='bold', ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='green', ax=ax)
        ax.set_title(f'DFS Traversal - Current Visiting Node: "{visited_nodes[-1]}" and Visited Nodes: {visited_nodes}')

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    If there is a cycle that is reachable from root, then this will see infinite recursion.
    G: the graph (must be a tree)
    root: the root node of the current branch
    - if the tree is directed and this is not given, 
    the root will be found and used
    width: horizontal space allocated for this branch
    - affects the distance between leaves
    vert_gap: gap between levels of hierarchy
    vert_loc: vertical location of root
    xcenter: horizontal location of root
    """

    pos = {root: (xcenter, vert_loc)}
    neighbors = list(G.neighbors(root))
    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos.update(hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, 
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx))
    return pos

if __name__ == "__main__":
    # Create the tree
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")

    # Create and visualize the graph
    G = graph.to_networkx_graph()

    # Define a hierarchical layout for tree visualization
    pos = hierarchy_pos(G, root="A")  # Generate the hierarchical positions

    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 10))
    plt.ion()  # Turn on interactive mode

    # Perform DFS and visualize
    dfs_result = graph.depthFirstSearch([], G, pos, ax)
    print(f"DFS Result: {dfs_result}")

    plt.ioff()  # Turn off interactive mode
    plt.show()
