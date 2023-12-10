class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count=1
        for i in edges[0]:
            for j in range(1,len(edges)):
                if i in edges[j]:
                    count+=1
            if count == len(edges):
                return i

        
