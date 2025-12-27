# Merge Two Sorted Singly Linked Lists
# Time Complexity: O(n + m) - single pass through both lists
# Space Complexity: O(1) - only relinks existing nodes



def merge_two_lists(l1,l2):

    dummy = tail = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2 
    return dummy.next


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next