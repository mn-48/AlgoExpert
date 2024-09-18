# # *#3.1 Time O(nlog(n)) | Space O(1)*

# def sortedSquaredArray(array):
#     # Write your code here.
#     new_array = [i*i for i in array] 
#     return sorted(new_array)


# Time O(n) | Space O(n)

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


