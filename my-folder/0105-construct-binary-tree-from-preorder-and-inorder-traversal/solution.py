# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        postindex=0
        def construct(starti,endi):
            nonlocal postindex
            if starti > endi:
                return None
            node=TreeNode(preorder[postindex])
            postindex+=1
            if starti == endi:
                return node
            Index=inorder.index(node.val)
            node.left=construct(starti,Index-1)
            node.right=construct(Index+1,endi)
            return node
        return construct(0,len(inorder)-1)
        
