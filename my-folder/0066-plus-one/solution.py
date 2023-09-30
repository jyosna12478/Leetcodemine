class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        for i in digits:
            res=res+str(i)
        s=str(int(res)+1)
        l=[]
        for i in range(0,len(s)):
            l.insert(i,int(s[i]))
        return l
        
        
        
