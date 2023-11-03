# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        curr1=root1
        curr2=root2

        if curr1 and curr2:
            curr1.val=curr1.val+curr2.val

            curr1.left=self.mergeTrees(curr1.left,curr2.left)
            curr1.right=self.mergeTrees(curr1.right,curr2.right)

            return curr1

        else:
            return curr1 or curr2
        
        """lif curr1 is None and curr2 is not None:
            curr1=TreeNode(curr2.val)
            return curr1

        elif curr2 is None and curr1 is not None:
            return curr1

        else:
            return None"""




        
