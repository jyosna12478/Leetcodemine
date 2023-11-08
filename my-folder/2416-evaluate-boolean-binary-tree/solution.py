# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            if root.val==0:
                return False
            else:
                return True
        else:
            root.left=self.evaluateTree(root.left)
            root.right=self.evaluateTree(root.right)

            if root.val==2:
                return root.left or root.right
            else:
                return root.left and root.right
        
