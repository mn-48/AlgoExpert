# Time Complexity O(nlog(n)) | Space Complexity O(1)*

def nonConstructibleChange(coins):
    coins.sort()
    # Write your code here.
    current_sum = 0
    for i in coins:
        if i > current_sum+1:
            break
        current_sum+=i
            
    return current_sum+1
