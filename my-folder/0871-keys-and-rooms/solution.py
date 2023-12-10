class Solution:
    visited=list()
    
    def helper_visited(self,rooms,n):

            for i in rooms[n]:
                if not self.visited[i]:
                    self.visited[i]=True
                    self.helper_visited(rooms,i)

    def canVisitAllRooms(self, rooms: List[List[int]],visited=list()) -> bool:
        self.visited=[False]*len(rooms)
        print(len(rooms))
        """for i in range(0,len(rooms)):
            self.visited.append(False)"""
        self.visited[0]=True

        self.helper_visited(rooms,0)
        print(self.visited)
        for u in range(len(self.visited)):
            if not self.visited[u]:
                return False
        return True

        


  


        
        
