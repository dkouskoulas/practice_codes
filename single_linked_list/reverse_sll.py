# Reverse Singly Linked List (Iterative)
# Time Complexity: O(n) - single pass through list
# Space Complexity: O(1) - only uses constant extra space

def reverse_list(head):

    prev = None 
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        
    return prev