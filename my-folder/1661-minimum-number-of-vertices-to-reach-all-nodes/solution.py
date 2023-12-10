class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        arr=[False]*n
        for src,des in edges:
            arr[des]=True
        
        unvisited=set()
        for u in range(n):
            if not arr[u]:
                unvisited.add(u)

        return unvisited
    
        
