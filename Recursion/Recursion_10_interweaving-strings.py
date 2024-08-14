# # O(2^(N+M)) Time | O(N+M) Space

# def interweavingStrings(one, two, three):
#     if len(three) != len(one) +len(two):
#         return False
#     return areInterweaven(one, two, three, 0, 0)

# def areInterweaven(one, two, three, i, j):
#     k = i+j
#     if k == len(three):
#         return True
    
#     if i< len(one) and one[i] == three[k]:
#         if areInterweaven(one, two, three, i+1, j):
#             return True
#     if j< len(two) and two[j] == three[k]:
#         if areInterweaven(one, two, three, i, j+1):
#             return True
        
#     return False

# O(NM)) Time | O(NM) Space

def interweavingStrings(one, two, three):
    if len(three) != len(one) +len(two):
        return False
    cache = [[None for j in range(len(two)+1)] for i in range(len(one)+1)]
    return areInterweaven(one, two, three, 0, 0, cache)

def areInterweaven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    
    k = i+j
    if k == len(three):
        return True
    
    if i< len(one) and one[i] == three[k]:
        cache[i][j] =  areInterweaven(one, two, three, i+1, j, cache)
        if cache[i][j]:
            return True
    if j< len(two) and two[j] == three[k]:
        cache[i][j] =  areInterweaven(one, two, three, i, j+1, cache)
        if cache[i][j]:
            return True
    cache[i][j] = False   
    return False

if __name__=="__main__":
    one = "algoexpert"
    two = "your-dream-job"
    three = "your-algodream-expertjob"
    
    ans = interweavingStrings(one, two, three)
    print(ans)
    # True