# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = [self]
        
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            
            for child in current.children:
                queue.append(child)
        return array
        


if __name__=="__main__":
    
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    
    ans = graph.breadthFirstSearch([])
    print(ans)
