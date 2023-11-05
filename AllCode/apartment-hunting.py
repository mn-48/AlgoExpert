# O(br) time | O(br) Space

def apartmentHunting(blocks, reqs):
    n = len(blocks)
    distance_storing = [dict() for _ in range(n)]

    # left --> right
    for i in range(n):
        for req in reqs:
            distance_storing[i][req] = float("inf")
            if blocks[i][req]:
                distance_storing[i][req] = 0
            elif i>0:
                distance_storing[i][req] = distance_storing[i-1][req]+1

    # right --> left
    for i in range(n-1, -1, -1):
        for req in reqs:
            if blocks[i][req]:
                distance_storing[i][req] = 0
            else:
                if i < n-1:
                    distance_storing[i][req] = min(distance_storing[i+1][req]+1, distance_storing[i][req])
                
    # compare
    res = [0, max(distance_storing[0].values())]

    for i in range(1, n):
        max_value = max(distance_storing[i].values())
        if res[1] > max_value:
            res[0] = i
            res[1] = max_value
    return res[0]

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False}, 
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))