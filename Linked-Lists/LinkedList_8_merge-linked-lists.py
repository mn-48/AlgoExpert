# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n+m) Time | O(1) Space
def mergeLinkedLists(headOne, headTwo):

    min, max = (headOne, headTwo) if headOne.value < headTwo.value else (headTwo, headOne)

    head = min
    while min and max:
        while min.next and min.next.value <= max.value:
            min = min.next
        temp = min.next
        min.next = max
        min = max
        max = temp
    return head
   