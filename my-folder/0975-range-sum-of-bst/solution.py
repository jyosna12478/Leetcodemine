# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int,sum1:int=0) -> int:
        if not root:
            return 0

        sum1 = 0

        if root.val >= low and root.val <= high:
            sum1 += root.val

        if root.left:
            sum1 += self.rangeSumBST(root.left, low, high)
        if root.right:
            sum1 += self.rangeSumBST(root.right, low, high)

        return sum1
        
