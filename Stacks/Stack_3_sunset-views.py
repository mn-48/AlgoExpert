# O(n) Time | O(n) Space
def sunsetViews(buildings, direction):
    ans = []
    maxi = float("-inf")
    
    if direction=="EAST":
        for i in range(len(buildings)-1,-1, -1 ):
            if buildings[i] > maxi:
                maxi = buildings[i]
                ans.append(i)
        return ans[::-1]
    else: 
         for i in range(len(buildings)):
            if buildings[i] > maxi:
                maxi = buildings[i]
                ans.append(i)
    return ans

