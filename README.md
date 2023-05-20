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
### 4. [https://www.algoexpert.io/questions/sorted-squared-array](https://www.algoexpert.io/questions/sorted-squared-array)

### ________________________________________________________________________________________________
### ________________________________________________________________________________________________
