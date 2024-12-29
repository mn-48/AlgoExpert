# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(m,n)) Time | O(max(m,n)) Space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkListHeadPointer = LinkedList(0)
    currentNode = newLinkListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0

        someOfValues = valueOne + valueTwo + carry

        newValue = someOfValues % 10
        newNode = LinkedList(newValue)

        currentNode.next = newNode
        currentNode = newNode

        carry = someOfValues // 10

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    

    return newLinkListHeadPointer.next
