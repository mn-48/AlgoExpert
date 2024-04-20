#  Time O(n^3) | O(n^2) Space
# def palindromePartitioningMinCuts(string):
    
#     palindromes = [[False] * len(string) for j in range(len(string))]
    
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             palindromes[i][j] = isPalindrome(string[i:j+1])
            
#     cuts = [float('inf')] * len(string)
    
#     for i in range(len(string)):
#         if palindromes[0][i]:
#             cuts[i] = 0
#         else:
#             for j in range(1, i+1):
#                 if palindromes[j][i]:
#                     cuts[i] = min(cuts[i], cuts[j-1]+1)
#     return cuts[-1]
                    
            
            
# def isPalindrome(string):
#     left = 0
#     right = len(string)-1
    
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
        
    
 #  Time O(n^2) | O(n^2) Space   
def palindromePartitioningMinCuts(string):
    
    palindromes = [[False] * len(string) for j in range(len(string))]
    
    for i in range(len(string)):
        palindromes[i][i] = True
        
    for length  in range(2, len(string)+1):
        for i in range(0, len(string)-length +1):
            j = i+length -1
            if length == 2:
                palindromes[i][j] = string[i]==string[j]
            else:
                palindromes[i][j]= string[i]==string[j] and palindromes[i+1][j-1]
            
            
    cuts = [float('inf')] * len(string)
    
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            for j in range(1, i+1):
                if palindromes[j][i]:
                    cuts[i] = min(cuts[i], cuts[j-1]+1)
    return cuts[-1]
                    
            
   
    
if __name__=="__main__":
    ans = palindromePartitioningMinCuts("noonabbad")
    print(ans)