'''
This module contains a function to convert a string representation of a linked list to a linked list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_from_string(s):
    '''
    Convert a string representation of a linked list to a linked list.
    '''
    if not s or s.lower() == 'none':
        return None
    s = s.split(' -> ')
    head = None
    curr = None
    for val in s:
        if val.lower() == 'none':
            break
        node = Node(int(val))
        if not head:
            head = node
            curr = node
        else:
            curr.next = node
            curr = curr.next
    return head
