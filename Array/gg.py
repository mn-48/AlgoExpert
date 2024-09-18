# time complexity O(n^2) | Space Complexity O(n)

def threeNumberSum(array, targetSum):
    # Write your code here.
    triplets = []
    array.sort()
    for i in range(len(array)-2):
        left = i+1
        right =len(array) - 1
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left +=1
                right -=1
                
            elif current_sum < targetSum:
                left +=1
            elif current_sum > targetSum:
                right -=1
    
    return triplets    
        
    
