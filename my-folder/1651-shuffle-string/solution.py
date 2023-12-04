class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """s=list(s)
        res=''
        for i in range (0,len(s)):

            s[i],s[indices[i]]=s[indices[i]],s[i]
        
        for i in s:
            res=res+i
        return res"""
        res = [''] * len(s)
        res1=""
        for i in range(len(s)):

            res[indices[i]] = s[i]
            print(res)

        for i in res:
            res1+=i

        return res1

