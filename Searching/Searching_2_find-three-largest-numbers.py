# # O(nlog(n)) | Space O(n)

# def findThreeLargestNumbers(array):
#     return sorted(array, reverse=True)[:3][::-1]


# O(n) Time | O(1) Space
 
def findThreeLargestNumbers(array):
    result = [float('-inf')] * 3
    for i in range(len(array)):
        if array[i] > result[2]:
            result[0] = result[1] 
            result[1] = result[2]
            result[2] = array[i]
        elif array[i] > result[1]:
            result[0] = result[1]
            result[1] = array[i]
        elif array[i] > result[0]:
            result[0] = array[i]
    return result
            
