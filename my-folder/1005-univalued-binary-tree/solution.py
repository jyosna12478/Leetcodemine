# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """if root is None:
            return True
        elif root and root.left and root.right:
            if root.val==root.left.val==root.right.val:
                left = self.isUnivalTree(root.left)
                right = self.isUnivalTree(root.right)
                return left and right
        elif root and root.right:
            return root.val==root.right.val
        elif root and root.left:
            return root.val==root.left.val
        else:
            return True"""
        if root is None:
            return True

        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        

        
