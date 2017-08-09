class NotBSTException(Exception):

    def __init__(self, message):
        super(NotBSTException, self).__init__(message)

class Node():

    def  __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def is_bst(node):
    if node.left:
        if node.value > node.left.value:      
            is_bst(node.left)
        else:
            raise NotBSTException('Not BST')

    if node.right:
        if node.value < node.right.value:
            is_bst(node.right)
        else:
            raise NotBSTException('Not BST')

def is_bst_2(node):

    if (node.left and node.value < node.left.value) or (node.right and node.value > node.right.value):
        return False
    
    if (node.left and not is_bst_2(node.left)) or (node.right and not is_bst_2(node.right)):
        return False

    return True

def construct_bst(node, value):

    if not node.value:
        node.value = value
    else:
        if node.value > value:
            if not node.left:
                node.left = Node(value)
            else:
                construct_bst(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                construct_bst(node.right, value)

def print_bst(node, identifier):

    if node:
        print '# %s :%s' % (identifier, node.value)

        print_bst(node.left, 'left of %s' % node.value)
        print_bst(node.right, 'right of %s' % node.value)
                
def main_2():
    node = Node(None)
    
    """
              10
           /     \
          4       11
         / \       \
        1   5      20
             \     /
              7   12
             / \    \
            6   9   13
    """
    construct_bst(node, 10)
    construct_bst(node, 4)
    construct_bst(node, 5)
    construct_bst(node, 11)
    construct_bst(node, 20)
    construct_bst(node, 12)
    construct_bst(node, 7)
    construct_bst(node, 1)
    construct_bst(node, 9)
    construct_bst(node, 13)
    construct_bst(node, 6)
    construct_bst(node, 21)
    
    print_bst(node, 'root')
    
def main_1():
    """
             10
          /      \
         5       12
       /   \    /   \
      4     7  11   15
    """
    n1 = Node(10)
    n2l1 = Node(5)
    n3r1 = Node(12)
    n4l2 = Node(4)
    n5r2 = Node(7)
    n6r3 = Node(15)
    n6l3 = Node(11)

    n1.right = n3r1
    n1.left = n2l1
    n2l1.left = n4l2
    n2l1.right = n5r2
    n3r1.right = n6r3
    n3r1.left = n6l3

    # Method 1: Via Exception
    try:
        is_bst(n1)
        print '# From Exception Method: BST'
    except NotBSTException:
        print '# From Exception Method: Not BST'
        
    # Method 2: Via Boolean
    if is_bst_2(n1):
        print '# From Boolean Method: BST'
    else:
        print '# From Boolean Method: Not BST'

if __name__ == '__main__':
    main_2()
