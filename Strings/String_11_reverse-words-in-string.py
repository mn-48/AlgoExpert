# # O(n) time | O(n) space - where n is the length of the string
# def reverseWordsInString(string):
#     characters = [char for char in string]
#     reverseListRange(characters, 0, len(characters) - 1)
    
#     startOfWord = 0
#     while startOfWord < len(characters):
#         endOfWord = startOfWord
#         while endOfWord < len(characters) and characters[endOfWord] != ' ':
#             endOfWord += 1
        
#         reverseListRange(characters, startOfWord, endOfWord - 1)
#         startOfWord = endOfWord + 1
    
#     return "".join(characters)

# def reverseListRange(list, start, end):
#     while start < end:
#         list[start], list[end] = list[end], list[start]
#         start += 1
#         end -= 1


# O(n) time | O(n) Space
def reverseWordsInString(string):
    return " ".join(string.split(" ")[::-1])
