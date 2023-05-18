#Time O(n^2)  | Space O(1) 
def twoNumberSum(array, targetSum):
    # Write your code here.
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i]+array[j] == targetSum:
                return [array[i] , array[j]]
    return []
        
   
