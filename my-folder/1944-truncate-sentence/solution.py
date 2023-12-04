class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1=s.split(" ")
        res=""
        for i in range(k-1):
            res+=s1[i]+" "

        res+=s1[k-1]
        return res

