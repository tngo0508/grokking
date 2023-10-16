from __future__ import print_function
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from print_list import print_list_with_forward_arrow

# Helper function
def merge_2_lists(head1, head2):  
    dummy = LinkedListNode(-1)
    prev = dummy  

    while head1 and head2:
        if head1.data <= head2.data:
            prev.next = head1
            head1 = head1.next
        else:
            prev.next = head2
            head2 = head2.next
        prev = prev.next

    if head1 is not None:
        prev.next = head1
    else:
        prev.next = head2

    return dummy.next

# Main function
def merge_k_lists(lists):  
    if len(lists) > 0:
        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i].head = merge_2_lists(lists[i].head, lists[i + step].head)
            step *= 2
        return lists[0].head
    return

# Driver code
def main():
    inputlists = [[[21, 23, 42], [1, 2, 4]],
        [[11, 41, 51], [21, 23, 42]],
        [[2], [1, 2, 4], [25, 56, 66, 72]],
        [[11, 41, 51], [2], [2], [2], [1, 2, 4]],
        [[10, 30], [15, 25], [1, 7], [3, 9], [100, 300], [115, 125], [10, 70], [30, 90]]
    ]
    inp_num = 1
    for i in inputlists:
        print(inp_num, ".\tInput lists:", sep = "")
        ll_lists = []
        for x in i:
            a = LinkedList()
            a.create_linked_list(x)
            ll_lists.append(a)
            print("\t", end = "")
            print_list_with_forward_arrow(a.head)
            print()
        inp_num += 1
        print("\tMerged list: \n\t", end = "")
        print_list_with_forward_arrow(merge_k_lists(ll_lists))
        print("\n", "-"*100, sep = "")

if __name__ == "__main__":
    main()