# O(n*lon(n)) Time | O(n) Space

def sweetAndSavory(dishes, target):
    sweet_dishes = sorted([dish for dish in dishes if dish <0 ], key=abs)
    savory_dishes = sorted([dish for dish in dishes if dish >0 ])
   
    ans = [0, 0]
    i, j = 0,0

    best = float('inf')
    while i < len(sweet_dishes) and j < len(savory_dishes):
        falvor = (sweet_dishes[i]+savory_dishes[j])
        if falvor <= target:
            current_difference  = target -falvor
            if  current_difference < best:
                ans = [sweet_dishes[i],savory_dishes[j]]
                best = current_difference
            j+=1
        else:
            i+=1
    return ans


dishes = [2, 5, -4, -7, 12, 100, -25]
target = -5
sweetAndSavory(dishes, target)