

def detect_cycle_lenght(head):
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_length = 1
            current = slow.next

            while current != slow:
                current = current.next
                cycle_length +=1

            return cycle_length
        
        return 0
