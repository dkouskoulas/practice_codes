


def reverse_list(head):

    prev = None
    cur = List(head)

    while cur:
        next = cur.next
        cur.next = prev 
        prev = cur
        cur = next

    return prev
