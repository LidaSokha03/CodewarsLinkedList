def swap_pairs(head):
    '''
    Swap every two adjacent nodes in a linked list and return its head.
    '''
    if not head or not head.next:
        return head

    curr = head
    head = curr.next
    prev = None

    while curr and curr.next:
        first = curr
        second = curr.next
        first.next = second.next
        second.next = first
        if prev:
            prev.next = second

        prev = first
        curr = first.next

    return head
