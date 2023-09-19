# Average O(n^2) Time | O(n^2) Space 
# Worst O(n^3) Time | O(n^2) Space 

def fourNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()
    n = len(array)

    for i in range(0, n-3):
        for j in range(i+1, n-2):
            left = j+1
            right = n-1
            while left < right:
                total_sum = array[i] + array[j] + array[left] + array[right]
                if targetSum == total_sum:
                    result.append([array[i] , array[j] , array[left] , array[right]])
                    left +=1
                    right-=1
                elif total_sum > targetSum :
                    right -=1
                    
                else:
                    left +=1
    return result


array = [7,6,4,-1,1,2]
targetSum = 16

print(fourNumberSum(array, targetSum))
