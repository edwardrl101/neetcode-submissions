# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = root.val
        def inOrderTraversal(node):
            if not node:
                return
            
            inOrderTraversal(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
            inOrderTraversal(node.right)
        
        inOrderTraversal(root)
        return self.res
