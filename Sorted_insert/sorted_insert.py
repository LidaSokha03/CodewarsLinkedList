'''
This module contains a function to insert a node in a sorted singly linked list.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    '''
    Inserts a node in a sorted singly linked list.
    '''
    if not head:
        return Node(data)
    if data < head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    new_node = Node(data)

    curr = head
    while curr.data < new_node.data and curr.next and curr.next.data < new_node.data:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head
