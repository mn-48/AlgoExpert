# O(n*n!) Time | O(n*n!) Space
from itertools import permutations
def getPermutations(array):
    perms_dic = permutations(array)
    ans = []
    if len(array) == 0:
        return []
    for p in perms_dic:
        ans.append(list(p))
    return ans

