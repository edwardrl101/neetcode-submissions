# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                v = q.popleft()
                if _ == n-1:
                    res.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)


        return res