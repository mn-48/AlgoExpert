#  O(nlog(n)) Time | O(n) Space
 
import heapq

def laptopRentals(times):
    times.sort(key=lambda x:x[0])
    # print(times)
    rented = []

    for start, end in times:
        if rented and rented[0] <= start:
            heapq.heappop(rented)
        heapq.heappush(rented, end)

    return len(rented)


if __name__=="__main__":
    input = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
    ans =  laptopRentals(input)
    print(ans)