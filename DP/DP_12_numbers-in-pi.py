# # This file is initialized with a code version of this
# # question's sample test case. Feel free to add, edit,
# # or remove test cases in this file as you see fit!

# import program
# import unittest


# PI = "3141592653589793238462643383279"


# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         numbers = [
#             "314159265358979323846", # 314159265358979323846 | 2643383279
#             "26433", # 314159265358979323846 | 26433 | 83279
#             "8",  # 314159265358979323846 | 26433 | 8 | 3279
#             "3279", # 314159265358979323846 | 26433 | 8 | 3279
#             "314159265", # 314159265 | 358979323846 | 26433 | 8 | 3279
#             "35897932384626433832", # 314159265 | 35897932384626433832 | 79
#             "79", # 314159265 | 35897932384626433832 | 79
#         ]
#         self.assertEqual(program.numbersInPi(PI, numbers), 2)


# 0(n^3+m) Time | O(n+m) space
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx:i+1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i+1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]
