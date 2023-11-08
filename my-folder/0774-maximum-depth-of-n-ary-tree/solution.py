"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        else:
            sum1=1
            for i in root.children:
                n=1+self.maxDepth(i)
                if n>sum1:
                    sum1=n
            return sum1
        
