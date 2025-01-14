# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space


def rearrangeLinkedList(head, k):
    samller_than_K_head = samller_than_K_tail = LinkedList(None)
    equal_to_K_head = equal_to_K_tail = LinkedList(None)
    greater_than_K_head = greater_than_K_tail = LinkedList(None)

    current = head
    while current:
        if current.value < k:
            samller_than_K_tail.next = current
            samller_than_K_tail = samller_than_K_tail.next
        elif current.value == k:
            equal_to_K_tail.next = current
            equal_to_K_tail = equal_to_K_tail.next
        else:
            greater_than_K_tail.next = current
            greater_than_K_tail = greater_than_K_tail.next
        current = current.next

        samller_than_K_tail.next = equal_to_K_head.next
        equal_to_K_tail.next = greater_than_K_head.next
        greater_than_K_tail.next = None

    return samller_than_K_head.next
