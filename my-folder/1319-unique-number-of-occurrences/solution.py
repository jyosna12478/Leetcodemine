class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        count=0
        for i in arr:
            d[i]=0
        for i in arr:
            d[i]=d[i]+1
        s=set(d.values())
        l=list(d.values())
        if len(s)==len(l):
            return True
        else:
            return False



            
