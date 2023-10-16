from linked_list import LinkedList
from linked_list_node import LinkedListNode
from swap_two_nodes import swap
            
def swap_nodes(head, k):
    count = 0
    curr = head
    sentinel = LinkedListNode(0, head)
    prev_front = sentinel
    next_end = None

    while curr and count < k - 1:
        prev_front = prev_front.next
        curr = curr.next
        count += 1
    
    front = curr
    next_front = front.next
    end = head
    prev_end = sentinel
    while curr and curr.next:
        prev_end = prev_end.next
        end = end.next
        curr = curr.next

    next_end = end.next

    prev_front.next = end
    if end != next_front:
        end.next = next_front
    else:
        end.next = front
    front.next = next_end
    if prev_end != front:
        prev_end.next = front

    return sentinel.next

