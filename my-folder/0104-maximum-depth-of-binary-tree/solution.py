# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr=root
        lengthl=1
        lengthr=1

        if curr is None:
            return 0
        else:
            lengthl+=self.maxDepth(curr.left)
            lengthr+=self.maxDepth(curr.right)

            return max (lengthl,lengthr)

