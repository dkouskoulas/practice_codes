# Floyd's Cycle Detection (Tortoise and Hare)
# Time Complexity: O(n) - traverses list at most twice
# Space Complexity: O(1) - only uses two pointers

#this detects cycle and returns the start point 



def detect_cycle(head):

    slow = fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    slow = head 

    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow 
