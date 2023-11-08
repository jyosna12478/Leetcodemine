# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],temp=0) -> int:
        res = 0
        if root.left == root.right == None: return (temp<<1) + root.val
        if root.left:  res += self.sumRootToLeaf(root.left, (temp<<1) + root.val)
        if root.right: res += self.sumRootToLeaf(root.right,(temp<<1) + root.val) 
        return res
        
        
