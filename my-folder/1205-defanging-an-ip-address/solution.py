class Solution:
    def defangIPaddr(self, address: str) -> str:
        if (address.find(".")!=-1):
            res=""
            for i in address:
                if(i=="."):
                    res=res+"[.]"
                else:
                    res=res+i
            return res
