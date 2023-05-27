# AlgoExpert
## Array
### 1. [https://www.algoexpert.io/questions/two-number-sum](https://www.algoexpert.io/questions/two-number-sum)


*#1.1 Time O(n^2)  | Space O(1)*
```
def twoNumberSum(array, targetSum):
    # Write your code here.
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i]+array[j] == targetSum:
                return [array[i] , array[j]]
    return []
```


*#1.2 Time O(n) Space O(n)*
```
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}

    for x in array:
        y = targetSum-x

        if y in nums:
            return [x, y]
        else:
            nums[x] = True

    return []
```
*#1.3 Time O(nlog(n)) Space O(1) with binary search*
```
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()

    n = len(array)
    left = 0
    right = n-1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1 
        elif array[left] + array[right] < targetSum:
            left += 1 
    return []

```
### ________________________________________________________________________________________________
    

### 2. [https://www.algoexpert.io/questions/validate-subsequence](https://www.algoexpert.io/questions/validate-subsequence)

*#2.1 Time O(n) | Space O(1)*
```
def isValidSubsequence(array, sequence):
    # Write your code here.  
    arr_indx = 0
    seq_indx = 0

    while arr_indx<len(array) and seq_indx< len(sequence):
        if array[arr_indx] == sequence[seq_indx]:
            seq_indx +=1
        
        arr_indx += 1
    return seq_indx ==len(sequence)
```

*#2.2 Time O(n) | Space O(1)*
```
def isValidSubsequence(array, sequence):
    seq_indx = 0
    for a in array:
        if seq_indx==len(sequence):
            return True
        if sequence[seq_indx] == a:
            seq_indx += 1
    return seq_indx == len(sequence)
```

### ________________________________________________________________________________________________

### 3. [https://www.algoexpert.io/questions/sorted-squared-array](https://www.algoexpert.io/questions/sorted-squared-array)

*#3.1 Time O(n^2) | Space O(1)*
```
def sortedSquaredArray(array):
    # Write your code here.
    new_array = [i*i for i in array] 
    return sorted(new_array)

```
*#3.2 Time O(n) | Space O(n)*
```
def sortedSquaredArray(array):
    ans = [0 for _ in array]
    small_val_indx = 0
    large_val_indx = len(array)-1

    for i in reversed(range(len(array))):
        small_val = array[small_val_indx]
        large_val = array[large_val_indx]

        if small_val*small_val < large_val*large_val:
            ans[i] = large_val*large_val
            large_val_indx -= 1
        else:
            ans[i] = small_val*small_val
            small_val_indx += 1
    return ans

```


### 4. [https://www.algoexpert.io/questions/tournament-winner](https://www.algoexpert.io/questions/tournament-winner)
*# Time Complexity O(n) | Space Complexity O(n)*
```
def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    for c, r in zip(competitions, results):
        if r==1:
            scores[c[0]] = scores.get(c[0], 0)+3
        else:
            scores[c[1]] = scores.get(c[1], 0)+3
           
    best_team = max(scores, key=lambda k: scores[k])
    return best_team
```

### 5. [https://www.algoexpert.io/questions/non-constructible-change](https://www.algoexpert.io/questions/non-constructible-change)
*# Time Complexity O(nlog(n)) | Space Complexity O(1)*
```
def nonConstructibleChange(coins):
    coins.sort()
    # Write your code here.
    current_sum = 0
    for i in coins:
        if i > current_sum+1:
            break
        current_sum+=i
            
    return current_sum+1

```
### 6. [https://www.algoexpert.io/questions/three-number-sum](https://www.algoexpert.io/questions/three-number-sum)
*# # time complexity O(n^2) | Space Complexity O(n)*
```
def threeNumberSum(array, targetSum):
    # Write your code here.
    triplets = []
    array.sort()
    for i in range(len(array)-2):
        left = i+1
        right =len(array) - 1
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left +=1
                right -=1
                
            elif current_sum < targetSum:
                left +=1
            elif current_sum > targetSum:
                right -=1
    
    return triplets    
        
    


```
### ________________________________________________________________________________________________
### ________________________________________________________________________________________________
