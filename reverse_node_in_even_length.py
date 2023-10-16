from linked_list import LinkedList

def reverse_group(head, l):
  length = l
  curr = head
  prev = None
  next_node = None
  while curr and length > 0:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
    length -= 1
  return prev, head, curr

def reverse_even_length_groups(head):
  l = 1
  prev = head
  curr = head
  while curr:
    count = 0
    tracker = curr
    while tracker and count < l:
      count += 1
      tracker = tracker.next
    if count % 2 == 0:
      start, end, next_curr = reverse_group(curr, l)
      prev.next = start
      end.next = next_curr
      prev = end
      curr = end.next
    else:
      i = 0
      while curr and i < l:
        curr = curr.next
        i += 1
    l += 1
  return head

