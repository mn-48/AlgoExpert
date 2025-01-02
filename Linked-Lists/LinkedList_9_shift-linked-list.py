# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    p2=p3=p1= head
    totalNode = 0

    while head:
        totalNode +=1
        head = head.next
        
    k = k% totalNode

    if k==0:
        return p1
        
    s = 0
    while  s<k:
        p2 = p2.next
        s+=1
        
    while p2.next:
        p2 = p2.next
        p3 = p3.next

    newHead = p3.next
    p2.next = p1
    p3.next = None

    return newHead
        

