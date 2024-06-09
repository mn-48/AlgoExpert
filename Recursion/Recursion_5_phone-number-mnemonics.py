# O(4^n*n) Time | O(4^n*n) Space

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    dict_numbers = {"1": "1",
                    "0": "0",
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz",
                    "10": " "
                    }
    result = [""]
    for digit in phoneNumber:
        lst = dict_numbers[digit]
        new_result = []
        for char in lst:
            for val in result:
                new_result.append(val+char)
        result = new_result

    return result
