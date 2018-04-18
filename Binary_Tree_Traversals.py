"""

@author: Bhoomit Patel
Program for tree traversals in Python

"""

#A class for each node in a Tree
class Node:

    def __init__(self,key):

        self.left = None
        self.right = None
        self.value = key


#Function to do Pre-oreder Traversal (Visit - Left - Right)
def print_preorder(root):

    if root:

        print(root.value, end=" ")

        print_preorder(root.left)

        print_preorder(root.right)

    return

#Function to do In-order Traversal(Left - Visit - Right)
def print_inorder(root):
    if root:
        print_inorder(root.left)

        print(root.value,end=" ")

        print_inorder(root.right)

    return



#Function to do Post-order Traversal(Left - Right - Visit)
def print_postorder(root):
    if root:
        print_postorder(root.left)

        print_postorder(root.right)

        print(root.value,end=" ")


#Driver Program

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

"""
Visual Representation of the current Tree

                1
            /       \
        /               \
        2               3
    /       \
    4       5
    
    
"""

print ("Preorder traversal of binary tree is")
print_preorder(root)

print ("\nInorder traversal of binary tree is")
print_inorder(root)

print ("\nPostorder traversal of binary tree is")
print_postorder(root)