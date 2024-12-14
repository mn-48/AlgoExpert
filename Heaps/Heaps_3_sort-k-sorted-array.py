#  O(nlog(k)) Time | O(k) Space

import heapq
def sortKSortedArray(array, k):
    # Write your code here.
    sorted_idx = 0
    heap = array[sorted_idx: k+1]
    heapq.heapify(heap)

    for i in range(k+1, len(array)):
        array[sorted_idx] = heapq.heappop(heap)
        sorted_idx += 1
        heapq.heappush(heap, array[i])
    while len(heap) > 0:
        array[sorted_idx] = heapq.heappop(heap)
        sorted_idx += 1
    return array
