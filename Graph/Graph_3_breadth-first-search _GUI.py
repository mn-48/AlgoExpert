import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

def add_edges(graph, node):
    for child in node.children:
        graph.add_edge(node.name, child.name)
        add_edges(graph, child)

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)  
    if len(children) != 0:
        dx = width / len(children) 
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
    return pos

def visualize_bfs(root):
    G = nx.DiGraph()
    add_edges(G, root)

    # BFS traversal order
    bfs_order = root.breadthFirstSearch([])

    # Generate hierarchical positions
    pos = hierarchy_pos(G, root.name)
    
    # Set background color to green
    fig = plt.figure(facecolor='green')
    ax = fig.add_subplot(111)
    ax.set_facecolor('green')
    
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)

    # Highlight nodes according to BFS order
    for i, node in enumerate(bfs_order):
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange')
        plt.title(f"BFS Step {i + 1}: Visiting {node} , Graph Vidited Nodes: {bfs_order[:i+1]}" )
        plt.draw()  # Update the figure with the new title
        plt.pause(1)

    plt.show()

if __name__ == "__main__":
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")

    visualize_bfs(graph)
