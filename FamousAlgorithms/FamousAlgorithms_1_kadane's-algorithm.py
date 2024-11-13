# O(n) Time | O(1) 
def kadanesAlgorithm(array):
    # Write your code here.
    max_sum, current_sum = float('-inf'), 0
    for num in array:
        current_sum += num
        max_sum, current_sum = max(max_sum, current_sum), max(0, current_sum)
    return max_sum
if __name__=="__main__":
    # ans = kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])
    ans = kadanesAlgorithm([-1, -2, -3, -5])
    print(ans)