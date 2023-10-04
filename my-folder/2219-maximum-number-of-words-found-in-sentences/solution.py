class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for i in sentences:
            k=i.split(" ")
            o=len(k)
            if (o>maximum):
                maximum=o
        return maximum
        
