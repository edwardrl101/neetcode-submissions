# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        self.bst = True
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.res and node.val <= self.res[-1]:
                self.bst = False
                return
            self.res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return self.bst