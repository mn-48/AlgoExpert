# # O(4^n*n) Time | O(4^n*n) Space

# def phoneNumberMnemonics(phoneNumber):
#     # Write your code here.
#     dict_numbers = {"1": "1",
#                     "0": "0",
#                     "2": "abc",
#                     "3": "def",
#                     "4": "ghi",
#                     "5": "jkl",
#                     "6": "mno",
#                     "7": "pqrs",
#                     "8": "tuv",
#                     "9": "wxyz",
#                     "10": " "
#                     }
#     result = [""]
#     for digit in phoneNumber:
#         lst = dict_numbers[digit]
#         new_result = []
#         for char in lst:
#             for val in result:
#                 new_result.append(val+char)
#         result = new_result

#     return result



# O(4^n*n) Time | O(4^n*n) Space

DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d","e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j","k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w","x", "y", "z"],
}

def phoneNumberMnemonics(phoneNumber):
    # print(DIGIT_LETTERS)
    # print(phoneNumber)
    currentMonomic = ["0"] * len(phoneNumber)
    monomicFound = []

    phoneNumberMnemonicsHelper(0, phoneNumber, currentMonomic, monomicFound)

    return monomicFound


def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMonomic, monomicFound):
    if idx == len(phoneNumber):
        monomic = ''.join(currentMonomic) #O(n)
        monomicFound.append(monomic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currentMonomic[idx] = letter
            phoneNumberMnemonicsHelper(idx+1, phoneNumber, currentMonomic, monomicFound)




if __name__ == "__main__":
    phoneNumber = "1905"
    ans = phoneNumberMnemonics(phoneNumber)

