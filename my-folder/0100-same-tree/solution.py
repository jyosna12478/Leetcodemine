# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        elif not p and q:
            return False
        
        elif not q and p:
            return False
        
        elif p.val==q.val:
            c=True
            left=self.isSameTree(p.left,q.left)
            right=self.isSameTree(p.right,q.right)

            return left and  right and c
        else:
            return False
