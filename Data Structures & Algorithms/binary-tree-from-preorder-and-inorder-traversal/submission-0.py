# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        def build(l: int, r: int):
            if l > r:
                return None
            n = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(n)
            idx = index[n]

            
            node.left = build(l, idx-1)
            node.right = build(idx+1, r)
            return node

                
        return build(0, len(inorder)-1)


        