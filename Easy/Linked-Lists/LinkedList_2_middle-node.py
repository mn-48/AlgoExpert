# O(n) Time | O(1) Space

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slower = linkedList
    faster = linkedList
    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next
        
    return slower
