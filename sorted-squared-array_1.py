# *#3.1 Time O(n^2) | Space O(1)*

def sortedSquaredArray(array):
    # Write your code here.
    new_array = [i*i for i in array] 
    return sorted(new_array)