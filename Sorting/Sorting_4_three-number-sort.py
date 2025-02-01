# # O(n) Time | O(1) Space

# def threeNumberSort(array, order):
#     index = 0
#     for i in range(2):
#         val = order[i]
#         for j in range(len(array)):
#             if array[j] == val:
#                 array[j], array[index] = array[index], array[j]
#                 index +=1
#     return array
   


# # O(n) Time | O(1) Space
def threeNumberSort(array, order):
    firstVal = order[0]
    secondVal= order[1]

    firstIdx = 0
    secondIdx = 0
    thirdIdx = len(array)-1

    while secondIdx <= thirdIdx:
        if array[secondIdx] == firstVal:
            swap(firstIdx, secondIdx, array)
            firstIdx +=1
            secondIdx +=1
        elif array[secondIdx] == secondVal:
            secondIdx += 1
        else:
            swap(secondIdx, thirdIdx, array)
            thirdIdx -=1
            
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

if __name__=="__main__":
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    ans = threeNumberSort(array, order)
    print(ans)