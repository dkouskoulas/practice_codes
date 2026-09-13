

def has_cycle(head):

    slow = fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # detected cycle
            length = 1
            fast = fast.next
            while slow != fast:
                fast= fast.next
                length += 1 
            return length

    return 0