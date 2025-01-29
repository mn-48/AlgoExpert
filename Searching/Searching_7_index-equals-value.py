# # O(n) Time | O(1) Space
# def indexEqualsValue(array):
#     for i in range(len(array)):
#         if i == array[i]:
#             return i
#     return -1

# O(log(n)) Time | O(1) Space
def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    index = -1
    while left <= right:
        mid = (left+right)//2
        midVal = array[mid]
        if mid < midVal:
            right = mid - 1
        elif mid > midVal:
            left = mid + 1
        else:
            index = mid
            right = mid - 1
    return index


if __name__ == "__main__":
    array = [-5, -3, 0, 3, 4, 5, 9]
    ans = indexEqualsValue(array)
    print(ans)
