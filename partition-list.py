# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        hash_map = defaultdict(list)
        curr = head
        while curr:
            if curr.val < x:
                hash_map['less'].append(curr)
            else:
                hash_map['greater'].append(curr)
            
            curr = curr.next
        
        curr = dummy
        less = deque(hash_map['less'])
        greater = deque(hash_map['greater'])

        while less and greater:
            while less and less[0].val <= greater[0].val:
                smaller_node = less.popleft()
                curr.next = smaller_node
                curr = curr.next
            curr.next = greater.popleft()
            curr = curr.next

        while less:
            node = less.popleft()
            curr.next = node
            curr = curr.next
        
        while greater:
            node = greater.popleft()
            curr.next = node
            curr = curr.next
        
        curr.next = None

        return dummy.next



# EdiApproach 1: Two Pointer Approach

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next