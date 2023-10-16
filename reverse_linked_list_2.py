from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def reverse_list(left_node, right_node):
  # print(right_node.data)
  right_node.next = None
  prev = None
  curr = left_node
  next_node = None
  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
    
            
def reverse_between(head, left, right):
  sentinel = LinkedListNode(0, head)
  curr = head
  prev_left = sentinel
  next_right = None
  right_node = None

  for _ in range(left - 1):
    prev_left = prev_left.next
    curr = curr.next
  
  left_node = curr

  curr = head
  for _ in range(right - 1):
    curr = curr.next

  right_node = curr

  next_right = right_node.next

  reverse_list(left_node, right_node)

  prev_left.next = right_node
  left_node.next = next_right
  return sentinel.next
