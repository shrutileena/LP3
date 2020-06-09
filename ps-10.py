class node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def isBst(root, left, right):
    if root == None:
        return True

    if (left != None and root.data <= left.data):
        return False

    if (right != None and root.data >= right.data):
        return False

    return isBst(root.left_child, left, root) and isBst(root.right_child, root, right)

if __name__ == '__main__':
    root = node(2)
    root.left_child = node(1)
    root.right_child = node(3)

    if (isBst(root,None,None)):
        print("Is BST")
    else:
        print("Not a BST")

    root = node(1)
    root.left_child = node(2)
    root.right_child = node(3)

    if (isBst(root,None,None)):
        print("Is BST")
    else:
        print("Not a BST")