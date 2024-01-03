# #  O(n^2) Time | O(n) Space

# def rightSmallerThan(array):
#     ls = []
#     for i in range(len(array)-1):
#         cnt = 0
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 cnt+=1
#         ls.append(cnt)
#     return ls+[0]

# # array = [8, 5, 11, -1, 3, 4, 2]
# # # expected = [5, 4, 4, 0, 1, 1, 0]
# # print(rightSmallerThan(array))


# =================================================
#  O(nlon(n)) Time | O(n) Space
import bisect

def rightSmallerThan(array):
    sorted_array = []
    results = [0] * len(array)
    for i in reversed(range(len(array))):
        results[i] = bisect.bisect_left(sorted_array, array[i])
        print(sorted_array)
        bisect.insort(sorted_array, array[i])
    return results

# array = [8, 5, 11, -1, 3, 4, 2]
# # expected = [5, 4, 4, 0, 1, 1, 0]
# print(rightSmallerThan(array))
