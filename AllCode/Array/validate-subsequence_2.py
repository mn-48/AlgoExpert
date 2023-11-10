# Time O(n) | Space O(1)

def isValidSubsequence(array, sequence):
    seq_indx = 0
    for a in array:
        if seq_indx==len(sequence):
            return True
        if sequence[seq_indx] == a:
            seq_indx += 1
    return seq_indx == len(sequence)
