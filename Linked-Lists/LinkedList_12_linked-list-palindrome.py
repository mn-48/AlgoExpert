# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space
def linkedListPalindrome(head):
    slow_node = head
    fast_node = head

    while fast_node is not None and fast_node.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    reversed_second_half_node = reversedLinkedList(slow_node)
    first_half_node = head

    while reversed_second_half_node is not None:
        if first_half_node.value != reversed_second_half_node.value:
            return False
        first_half_node = first_half_node.next
        reversed_second_half_node = reversed_second_half_node.next
    return True

def reversedLinkedList(head):
    previous_node = None
    currrent_node = head
    while currrent_node is not None:
        next_node = currrent_node.next
        currrent_node.next = previous_node
        previous_node = currrent_node
        currrent_node = next_node
    return previous_node
