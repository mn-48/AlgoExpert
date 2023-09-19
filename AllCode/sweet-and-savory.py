# O(n*lon(n)) Time | O(n) Space

def sweetAndSavory(dishes, target):
    dishes = sorted(dishes)
    sweet_dishes = []
    savory_dishes = []
    for num in dishes:
        if num < 0:
            sweet_dishes.append(abs(num))
        else:
            savory_dishes.append(num)
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


