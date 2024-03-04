# O(n) Time | O(1) Space

# Very short solution time: O(n), space: O(1)
# Explanation
# This solution can be interpreted as a DP solution.
# In this code are considered the total area from left (A) and total area from right (B) both of them are bounded by imaginary bars.
# The result is computed as the intersections of A and B, which can be computes as A intersection B = A+B- (A union B), where the union is just the contour of the bars.

def waterArea(heights):
    n = len(heights)
    maxH = max(heights, default=0)
    _sum = sum(heights)
    # print("_sum: ", _sum)
    contour = (maxH*n)-_sum
    # print("contour: ", contour)
    
    leftMax = 0
    leftArea=0
    for i in heights:
        leftMax = max(leftMax, i)
        leftArea += leftMax-i
        
    rightMax = 0
    rightArea = 0
    for i in range(n-1, -1, -1):
        rightMax = max(rightMax, heights[i])
        rightArea += rightMax - heights[i]
    # print(f"leftArea:{leftArea}, rightArea:{rightArea}, contour:{contour},")
    return leftArea + rightArea - contour
        
if __name__=="__main__":
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    # ans = 4
    print(waterArea(heights))

