#  O(nlog(n)) Time | O(n) Space
 
# import heapq

# def laptopRentals(times):
#     times.sort(key=lambda x:x[0])
#     # print(times)
#     rented = []

#     for start, end in times:
#         if rented and rented[0] <= start:
#             heapq.heappop(rented)
#         heapq.heappush(rented, end)

#     return len(rented)



# O(nlog(n)) Time | O(n) Space
def laptopRentals(times):
    if len(times) == 0:
        return 0
    usedLaptops = 0
    startTimes = sorted([t[0] for t in times])
    endTimes = sorted([t[1] for t in times])

    i = 0
    j = 0 
    while i < len(times):
        if startTimes[i] >= endTimes[j]:
            usedLaptops -= 1
            j+=1
        usedLaptops += 1
        i +=1
    
    return usedLaptops



if __name__=="__main__":
    input = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
    ans =  laptopRentals(input)
    print(ans)