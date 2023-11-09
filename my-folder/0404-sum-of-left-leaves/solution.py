# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum1 = 0

        if root.left and not root.left.left and not root.left.right:
            sum1 += root.left.val

        sum1 += self.sumOfLeftLeaves(root.left)
        sum1 += self.sumOfLeftLeaves(root.right)

        return sum1

        
