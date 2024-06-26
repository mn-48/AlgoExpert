# # O(n) Time  | O(1) space
# def isPalindrome(string):
#     # Write your code here.
#     return string == string[::-1]

# O(n) Time | O(1) Space

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string)-1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        
        leftIdx += 1
        rightIdx -= 1
    return True
    
    
