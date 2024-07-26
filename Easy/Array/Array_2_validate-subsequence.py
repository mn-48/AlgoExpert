# # Time O(n) | Space O(1)

# def isValidSubsequence(array, sequence):
#     seq_indx = 0
#     for a in array:
#         if seq_indx==len(sequence):
#             return True
#         if sequence[seq_indx] == a:
#             seq_indx += 1
#     return seq_indx == len(sequence)


# Time O(n) | Space O(1)

def isValidSubsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0
    
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx +=1
    return seq_idx == len(sequence)
            
   

if __name__=="__main__":
    ans = isValidSubsequence(list("codeforces"), list("forces"))
    print(ans)
        