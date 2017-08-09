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

def main():
    """
              10
          /        \
         5          12
       /   \       /   \
      4    7      11   15
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
    main()
