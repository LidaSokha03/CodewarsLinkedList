'''
This module contains a function to move the first node from one linked list to another.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''
    Moves the first node from the source list to the front of the destination list.
    '''
    if not source:
        raise Exception
    new_source = source.next
    new_dest = source
    new_dest.next = dest
    return Context(new_source, new_dest)
