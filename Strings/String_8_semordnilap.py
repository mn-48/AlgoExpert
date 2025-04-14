
# # O(n^3) Time | O(n) Space
# def longestPalindromicSubstring(string):
#     longest = ""
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             substring = string[i:j+1]
#             if len(substring) > len(longest) and isPalindrome(substring):
#                 longest = substring
#     return longest

# def isPalindrome(string):
#     left = 0
#     right  = len(string) -1

#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right  -= 1
#     return True

# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]