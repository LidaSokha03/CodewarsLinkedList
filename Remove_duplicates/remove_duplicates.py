'''
This module contains a function to remove duplicates from a linked list.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''
    Remove duplicates from a linked list.
    '''
    data = set()
    if not head:
        return None
    if not head.next:
        return head

    curr = head
    prev = None
    while curr:
        if curr.data not in data:
            data.add(curr.data)
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next
    return head
