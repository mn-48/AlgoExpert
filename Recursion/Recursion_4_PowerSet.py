# O(n*2^n) Time | O(n*2^n) Space 

def powerset(array):
    subsets = [[]]
    
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset+[ele])
    return subsets

# O(n*2^n) Time | O(n*2^n) Space 

def powerset(array, idx=None):

    if idx == None:
        idx = len(array)-1
    elif idx <0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx-1)
    
    
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset+[ele])
    return subsets
