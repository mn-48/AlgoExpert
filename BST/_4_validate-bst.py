# O(N) Time | O(d) Space
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float('-inf'), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    # print(f"tree={tree}, minValue={minValue}, maxValue={maxValue}")

    # print(tree, minValue, maxValue)
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftValid =  validateBstHelper(tree.left, minValue, tree.value)
    return leftValid and validateBstHelper(tree.right,  tree.value, maxValue)



# ============================
if __name__=="__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print(validateBst(root))


