# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def inorderRecursion(self, root, inorder):

        if root is None:
            return

        self.inorderRecursion(root.left, inorder)
        inorder.append(root.val)
        self.inorderRecursion(root.right, inorder)


    def isValidBST(self, root):
        inorder = []

        self.inorderRecursion(root, inorder)

        for i in range(1, len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        return True

        