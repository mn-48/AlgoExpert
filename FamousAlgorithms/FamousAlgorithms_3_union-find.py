# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.

# # O(1) Time | O(1) space
# class UnionFind:
#     def __init__(self):
#         self.parents = {}

#     def createSet(self, value):
#         self.parents[value] = value

#     def find(self, value):
#         if value not in self.parents:
#             return None
#         while value != self.parents[value]:
#             value = self.parents[value]
#         return value


#     def union(self, valueOne, valueTwo):
#         if valueOne not in self. parents or valueTwo not in self.parents:
#             return
#         valueOneRoot = self.find(valueOne)
#         valueTwoRoot = self.find(valueTwo)
#         self.parents[valueTwoRoot]=valueOneRoot

class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) Time| O(1) Space
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # O(α(n)) aproximately O(1) Time| O(1) Space

    def find(self, value):
        if value not in self.parents:
            return None
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    # O(α(n)) aproximately O(1) Time | O(1) Space

    def union(self, valueOne, valueTwo):
        if valueOne not in self. parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)

        if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1
