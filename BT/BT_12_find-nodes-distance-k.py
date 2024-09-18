# O(n) Time | O(n) Space

from collections import defaultdict, deque

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    
    adj = defaultdict(list)
    def tree_to_graph(node, parent):
        if not node:
            return
        if node.left:
            adj[node.value].append(node.left.value)
        if node.right:
            adj[node.value].append(node.right.value)
        if parent:
            adj[node.value].append(parent)
        tree_to_graph(node.left, node.value)
        tree_to_graph(node.right, node.value)
        
    tree_to_graph(tree, None)

    Q = deque([(0, target)])
    seen = set()
    ans = []

    while Q:
        d, node = Q.popleft()
        if node in seen:
            continue
        if d>k:
            break
        if d==k:
            ans.append(node)
        seen.add(node)
        for nei in adj[node]:
            Q.append((d+1, nei))
    return ans
