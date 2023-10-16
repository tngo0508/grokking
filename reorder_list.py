from linked_list import LinkedList
from linked_list_node import LinkedListNode

def reverse_list(head):
    curr = head
    prev = None
    next_node = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # while curr:
    #     curr.next, prev, curr = prev, curr, curr.next
    return prev
            
def reorder_list(head):
    if not head:
        return
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    p1 = head
    p2 = reverse_list(slow)

    sentinel = LinkedListNode(-1, head)
    prev = sentinel
    p1 = head

    while p1 and p2:
        prev.next = p1
        p1 = p1.next
        prev = prev.next
        prev.next = p2
        p2 = p2.next
        prev = prev.next
        prev.next = None

    return sentinel.next
                                                                            


def reorder_list(head):
    if not head:
        return head
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    prev, curr = None, slow

    while curr:
        curr.next, prev, curr = prev, curr, curr.next     
    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    
    return head