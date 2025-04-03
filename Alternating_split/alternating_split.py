'''
This module contains a function to split a linked list into two lists
'''
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''
    Splits a linked list into two lists, one containing the elements at
    '''
    if not head or not head.next:
        raise Exception

    first_head = head
    second_head = head.next

    first = first_head
    second = second_head

    curr = second.next
    ind = 0

    while curr:
        if ind%2==0:
            first.next = curr
            first = first.next
        else:
            second.next = curr
            second = second.next
        curr = curr.next
        ind += 1

    first.next = None
    second.next = None

    return Context(first_head, second_head)
