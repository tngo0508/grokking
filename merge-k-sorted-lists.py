# Brute Force - TLE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        N = len(lists)
        hash_map = {}
        for i in range(N):
            hash_map[i] = lists[i]

        while curr:
            temp = []
            for i in range(N):
                curr_head = hash_map[i]
                if curr_head:
                    temp.append([curr_head.val, curr_head, i])
            
            if temp:
                temp.sort(key=lambda x: x[0])
                _, node, idx = temp[0]
                hash_map[idx] = node.next
                next_node = node
                curr.next = next_node
                next_node.next = None
            curr = curr.next
        
        return dummy.next
    
# Brute Force - Accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        N = len(lists)
        hash_map = {}
        for i in range(N):
            hash_map[i] = lists[i]

        while curr:
            node = ListNode(float('inf'))
            idx = 0
            for i in range(N):
                curr_head = hash_map[i]
                if curr_head and curr_head.val < node.val:
                    node = curr_head
                    idx = i
            
            if node.val != float('inf'):
                hash_map[idx] = node.next
                next_node = node
                curr.next = next_node
                next_node.next = None
            curr = curr.next
        
        return dummy.next
    
# Divide and conquer approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(p1, p2):
            dummy = ListNode(-1)
            curr = dummy
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            
            curr.next = p1 if p1 else p2
            return dummy.next


        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        p1 = self.mergeKLists(lists[:mid])
        p2 = self.mergeKLists(lists[mid:])
        return merge(p1, p2)