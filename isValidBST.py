"""
@author : Bhoomit Patel
"""

# To Validate if Binary Tree is BST
#Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        int_min = -4294267296
        int_max = 4294267296
        """
        :type root: TreeNode
        :rtype: bool
        """

        return (self.CheckBST(root, int_min, int_max))

    def CheckBST(self, root, leftmin, rightmax):

        if root is None:
            return True
        if root.val < leftmin or root.val > rightmax:
            return False

        return (self.CheckBST(root.left, leftmin, root.val - 1) and self.CheckBST(root.right, root.val + 1, rightmax))