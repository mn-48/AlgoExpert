# Time O(n) | Space O(n)
def longestPeak(array):
    n = len(array)
    i = 1
    ans = 0
    
    while i<n:
        cnt = 1
        
        if array[i-1] >= array[i]:
            i+=1
            continue
        while i<n and array[i-1] < array[i]:
            i+=1
            cnt+=1
        if i>=n or array[i-1] == array[i]:
            continue
        while i<n and array[i-1] > array[i]:
            i+=1
            cnt+=1
            
        ans = max(ans, cnt)
    return ans
    
    
    

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# longestPeak(array)
