'''
This module contains a function to convert a linked list to a string representation.
'''
def stringify(node):
    '''
    Convert a linked list to a string representation.
    '''
    result = []
    curr = node
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    if result != []:
        return ' -> '.join(result) +  ' -> None'
    return 'None'
