# Time O(n^2) | Space O(n)

def minimumAreaRectangle(points):
    visited = set()
    min_area = float("inf")

    for x1, y1 in points:
        for x2, y2 in visited:
            if (x1, y2) in visited and (x2, y1) in visited:
                area = abs(x2-x1) * abs(y2-y1)
                min_area = min(area, min_area)
        visited.add((x1, y1))
    return 0 if min_area==float("inf") else min_area


#=======================
'''
# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
        expected = 3
        actual = program.minimumAreaRectangle(input)
        self.assertEqual(actual, expected)


'''