def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0

    length = 1
    current = slow.next
    while current != slow:
        current = current.next
        length += 1

    return length