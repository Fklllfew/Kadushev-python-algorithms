class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror(left, right):
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False
    return (left.value == right.value
            and mirror(left.left, right.right)
            and mirror(left.right, right.left))

def issym(root):
    if root == None:
        return True
    return mirror(root.left, root.right)