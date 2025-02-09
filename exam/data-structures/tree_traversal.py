class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def inorder_traversal(self, root):
        dummy = root
        while dummy:
            dummy = dummy.left
            
        

    # Implement a recursive inorder traversal of the binary tree
