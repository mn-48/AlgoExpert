# O(log(n)) Time | O(1) Space

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array)-1)        

def shiftedBinarySearchHelper(array, target, left, right):  
    while left <= right:
        mid = (left + right) // 2
        potentialMatch = array[mid]
        leftNum = array[left]
        rightNum = array[right]
        if target == potentialMatch:
            return mid
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > potentialMatch and target <= rightNum:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__=="__main__":
    ans = shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33)
    print(ans)