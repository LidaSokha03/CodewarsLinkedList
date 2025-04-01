'''
Push and Build Linked List
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    '''
    Push a new node with the given data onto the front of the linked list.
    '''
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    '''
    Build a linked list with three nodes containing the values 1, 2, and 3.
    '''
    node3 = Node(3)
    node2 = Node(2)
    node2.next = node3
    head = Node(1)
    head.next = node2   
    return head
