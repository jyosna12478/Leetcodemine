class Solution:
    def reverse(string:str):
            return string[::-1]
    def invert(string:str):
        result=""
        for i in string:
            if i =="1":
                result+="0"
            else:
                result+="1"
        return result

    def binary_string(n):
        if n==1:
            return "0"
        else:
            return Solution.binary_string(n-1)+"1"+Solution.reverse(Solution.invert(Solution.binary_string(n-1)))

    def findKthBit(self, n: int, k: int) -> str:
        
        string=Solution.binary_string(n)
        print(string)
        return string[k-1]
        
