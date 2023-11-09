# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        
        min1 = float('inf')
        
        n = len(l)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(l[i] - l[j]) < min1:
                    min1 = abs(l[i] - l[j])
        
        return min1

