import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def reverse_list(head_node, end_node):
    prev = None
    next_node = None
    curr = head_node
    while curr != end_node:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev, head_node
    
def reverse_k_groups(head, k):
    sentinel = LinkedListNode(-1, head)
    curr = head
    prev = sentinel
    group_head = curr
    while True:
        for _ in range(k-1):
            if curr:
                curr = curr.next
            else:
                break
        
        if not curr:
            break

        next_node = curr.next
        new_group_head, end_group_node = reverse_list(group_head, next_node)
        prev.next = new_group_head
        end_group_node.next = next_node
        prev = end_group_node
        group_head = next_node
        curr = next_node

    return sentinel.next



