# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space


def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList
    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)

    reversedSecondHalfHead = reversedLinkedList(secondHalfHead)
    return interweaveLinkedList(firstHalfHead, reversedSecondHalfHead)


def splitLinkedList(linkedList):
    slow_node = linkedList
    fast_node = linkedList
    while fast_node is not None and fast_node.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    secondHalfHead = slow_node.next
    slow_node.next = None
    return secondHalfHead


def reversedLinkedList(linkedList):
    previous_node = None
    current_node = linkedList
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node


def interweaveLinkedList(firstHalfHead, secondHalfHead):
    firstHalfCurrent = firstHalfHead
    secondHalfCurrent = secondHalfHead
    while firstHalfCurrent is not None and secondHalfCurrent is not None:
        firstHalfNext = firstHalfCurrent.next
        secondHalfNext = secondHalfCurrent.next

        firstHalfCurrent.next = secondHalfCurrent
        secondHalfCurrent.next = firstHalfNext

        firstHalfCurrent = firstHalfNext
        secondHalfCurrent = secondHalfNext
    return firstHalfHead
