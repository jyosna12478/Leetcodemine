# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(node,l):
            if node is None:
                return None
            postorder(node.left,l)
            postorder(node.right,l)
            l.append(node.val)
        postorder(root,l)
        return l
        
