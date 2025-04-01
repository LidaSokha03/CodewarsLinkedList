'''
This module contains a function to get the nth node of a singly linked list.
'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    '''
    Returns the nth node of a singly linked list.
    '''
    len = 0
    curr = node
    while curr.next:
        len+=1 
        curr = curr.next
        
    if not node:
        raise Exception
    if index < 0 or not isinstance(index, int) or index > len:
        raise Exception
    num = 0
    curr = node
    for i in range(index+1):
        if i == index:
            return curr
        else:
            curr = curr.next
