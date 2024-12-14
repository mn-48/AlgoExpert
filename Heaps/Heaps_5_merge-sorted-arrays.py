import heapq
# nlog(k) Time | O(n) Space


def mergeSortedArrays(arrays):
    return list(heapq.merge(*arrays))


# import heapq
# # nlog(k) Time | O(n) Space
# def mergeSortedArrays(arrays):
#     merged = []
#     min_heap = [(array[0], 0, array) for i, array in enumerate(arrays)]

#     heapq.heapify(min_heap)

#     while min_heap:
#         minimum, i, array = heapq.heappop(min_heap)
#         merged.append(minimum)
#         i += 1
#         if i < len(array):
#             heapq.heappush(min_heap, (array[i], i, array))
#     return merged


if __name__ == "__main__":

    arrays = [
        [1, 5, 9, 21],
        [-1, 0],
        [-124, 81, 121],
        [3, 6, 12, 20, 150],
    ]
    ans = mergeSortedArrays(arrays)
    print(ans)
