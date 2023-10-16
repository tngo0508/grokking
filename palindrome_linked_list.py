from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list


def palindrome(head):
    if not head:
        return True
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr is not None:
        next_ptr = curr.next
        curr.next = prev
        prev = curr
        curr = next_ptr
    
    slow = head
    fast = prev
    while slow and fast:
        if slow.data != fast.data:
            return False
        slow = slow.next
        fast = fast.next
    
    return True

