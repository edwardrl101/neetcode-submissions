# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if (p and not q) or (q and not p) or (p.val != q.val):
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            if n.val == subRoot.val:
                if isSameTree(n, subRoot):
                    return True
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return False