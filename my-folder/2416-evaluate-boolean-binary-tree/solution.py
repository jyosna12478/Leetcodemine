# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        if not root.left and not root.right:
            if root.val==1:
                return True
            else:
                return False
        else:
            left=self.evaluateTree(root.left)
            m=root.val
            right=self.evaluateTree(root.right)

            if left==1:
                left=True
            else:
                left=False
            
            if right==1:
                right=True
            else:
                right=False

            if m==2:
                return left or right
            else:
                return left and right

            
        
