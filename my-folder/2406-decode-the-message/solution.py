class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        visited=[]
        key2=""
        res=""
        for i in key:
            if not i in visited and i!=" ":
                visited.append(i)
                key2+=i

        #print(key2)
        
        alpha="abcdefghijklmnopqrstuvwxyz"

        for i in message:
            if i!=" ":
                k=key2.find(i)
            #print(k)

                res+=alpha[k]
            else:
                res+=" "

        return res


        
