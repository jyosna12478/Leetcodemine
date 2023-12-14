# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicti=dict()
        def helper_func(root):
            if root is None:
                return 
            else:
                if root.val in dicti:
                    dicti[root.val]+=1
                else:
                    dicti[root.val]=1
                helper_func(root.left)
                helper_func(root.right)


        helper_func(root)
        max_key=[]
        max_value=0
        for key,value in dicti.items():
            if value>=max_value:
                max_value=value
                
        for key in dicti:
            if dicti[key]==max_value:
                max_key.append(key)

        return max_key

        
