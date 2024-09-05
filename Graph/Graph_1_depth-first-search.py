# O(V+E) Time | O(V) Space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V+E) Time | O(V) Space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for clild in self.children:
            clild.depthFirstSearch(array)
        return array
            

if __name__ == "__main__":
    '''
        graph =  A
               / | \
              B  C  D
            /  \   / \
           E    F  G  H
               / \  \ 
              I   J  K

        DFS = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    '''
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    print(graph.depthFirstSearch([]))

    '''
    
    
    '''