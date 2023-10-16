from linked_list_node import *
from linked_list import *


def swap_pairs(head):
    sentinel = LinkedListNode(0, head)
    curr = head
    prev = sentinel
    while curr and curr.next:
        next_node = curr.next.next
        prev.next = curr.next
        curr.next.next = curr
        curr.next = next_node
        prev = curr
        curr = next_node
    return sentinel.next
