# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None

        def in_order(node):
            if not node:
                return True
            if not in_order(node.left):
                return False
            if self.prev and node.val <= self.prev.val:
                return False
            self.prev = node
            return in_order(node.right)

        return in_order(root)


        
