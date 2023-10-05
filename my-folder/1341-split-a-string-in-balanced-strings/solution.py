class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        L=0
        R=0
        for i in s:
            if i=='L':
                L=L+1
            elif i=='R':
                R=R+1
            if (L==R):
                count=count+1
                L=0
                R=0
            

        return count
        
