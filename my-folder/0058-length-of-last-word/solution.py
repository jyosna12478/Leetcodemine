class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if (s.__contains__(" ")):
            s = s.split(" ")
            for i in range (len(s)-1,-1,-1):
                if (s[i]==''):
                    continue
                else:
                    return len(s[i])
        return len(s)
        
