# AlgoExpert
## Array
### 1. [https://www.algoexpert.io/questions/two-number-sum](https://www.algoexpert.io/questions/two-number-sum)
*# Time O(n) | Space O(1)*
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

### 2. [https://www.algoexpert.io/questions/validate-subsequence](https://www.algoexpert.io/questions/validate-subsequence)


