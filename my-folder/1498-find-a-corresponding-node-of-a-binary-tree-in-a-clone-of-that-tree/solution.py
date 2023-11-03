# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned ==None:
            return None
    
        if cloned.val==target.val:
            return cloned
        else:
            
            c=self.getTargetCopy(original,cloned.left,target)
            
            d=self.getTargetCopy(original,cloned.right,target)
            if (c ):
                return c
            else:
                return d
        
