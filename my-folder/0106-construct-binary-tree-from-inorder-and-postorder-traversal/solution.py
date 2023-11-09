# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postindex=len(postorder)-1
        def construct ( starti, endi):
            nonlocal postindex
            if starti > endi:
                return None
            node=TreeNode(postorder[postindex])
            postindex-=1
            if starti==endi:
                return node
            index=inorder.index(node.val)
            node.right=construct(index+1,endi)
            node.left=construct(starti,index-1)

            return node

        node=construct(0,len(inorder)-1)
        return node     
