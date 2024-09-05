
#  O(n) Time | O(1) Space
def hasSingleCycle(array):
    start_idx = 0
    num_element_visited = 0
    current_idx = 0
    
    while num_element_visited < len(array):
        if num_element_visited > 0 and current_idx == start_idx:
            return False
        num_element_visited += 1
        current_idx = getNextIdx(current_idx, array)
    return current_idx == start_idx

def getNextIdx(current_idx, array):
    jump = array[current_idx]
    
    next_idx = (current_idx + jump) % len(array)
    
    return next_idx if next_idx >= 0 else next_idx + len(array)    


if __name__=="__main__":
    array = [2, 3, 1, -4, -4, 2]
    
    ans = hasSingleCycle(array)
    print(ans)