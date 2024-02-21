# ==========================================================
# O(2^(m+n)) Time | O(m+n) Space

# def numberOfWaysToTraverseGraph(width, height):
#     if width==1 or height==1:
#         return 1
#     return numberOfWaysToTraverseGraph(width-1, height)+numberOfWaysToTraverseGraph(width, height-1)

# ==========================================================

#  _______________________________
# |___0__|___1__|__1____|__1______|
# |___1__|___2__|__3____|__4______|
# |___1__|___3__|__6____|__10_____|


# O(m*n) Time | O(m*n) Space
def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0]*(width+1) for y in range(height+1)]
    
    for widthIdx in range(1, width+1):
        for heightIdx in range(1, height+1):
            if widthIdx == 1 or heightIdx ==1:
                numberOfWays[widthIdx][heightIdx]=1
                
            else:
                numberOfWays[widthIdx][heightIdx]= numberOfWays[widthIdx-1][heightIdx]+ numberOfWays[widthIdx][heightIdx-1]
    return numberOfWays[width][height]

# ==================================================================


# # O(m+n) Time | O(1) Space
# '''width = 4, height =3
#  _______________________________
# |Start_|___R__|__R____|__R______|
# |___D__|______|_______|_________|
# |___D__|______|_______|__End____|

# '''
# import math 
# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     # (R+D)!/(R!*D|!)
#     return math.comb(width+height-2, width-1)

# O(m+n) Time | O(1) Space
def numberOfWaysToTraverseGraph(width, height):
    xDistanceToCorner = width-1
    yDistanceToCorner = height-1
    
    nominator = factorial(xDistanceToCorner+yDistanceToCorner)
    denominator = factorial(xDistanceToCorner)*factorial(yDistanceToCorner)
    
    return nominator//denominator
    
def factorial(n):
    res = 1
    for i in range(2,n):
        res*=i
    return res


if __name__=="__main__":
    width = 4
    height = 3
    print(numberOfWaysToTraverseGraph(width, height))