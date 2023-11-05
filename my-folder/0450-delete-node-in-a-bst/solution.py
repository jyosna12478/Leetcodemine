# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            if root.val==key:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    """f root.left.val < root.right.val:
                        node=root.right
                        node.left=root.left
                        root=node
                    else:
                        node=root.left
                        node.left=root.right
                        root=node"""
                    parent=root
                    succ=root.right
                    while succ.left is not None:
                        parent =succ
                        succ=succ.left
                    
                    if parent != root:
                        parent.left = succ.right
                    else:
                        parent.right = succ.right

                    root.val=succ.val
                    return root
            elif root.val> key:
                root.left=self.deleteNode(root.left,key)
            else:
                root.right=self.deleteNode(root.right,key)

            return root
        
