# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) Time | O(1) Space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestoral_history = set()
    
    while descendantOne and descendantOne.name:
        ancestoral_history.add(descendantOne.name)
        descendantOne = descendantOne.ancestor
        
    while descendantTwo and descendantTwo.name:
        if descendantTwo.name in ancestoral_history:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor
    return None




if __name__=="__main__":
    
    class AncestralTree(AncestralTree):
        def addDescendants(self, *descendants):
            for descendant in descendants:
                descendant.ancestor = self


    def new_trees():
        ancestralTrees = {}
        for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            ancestralTrees[letter] = AncestralTree(letter)
        return ancestralTrees

    
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    ans = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
    print(ans.name)