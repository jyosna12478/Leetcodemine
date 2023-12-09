class Solution:
    def fib(self, n: int, prev=0,curr=1) -> int:
        """f n==0:   #non tail recursion
            return 0
        if n==1:
            return 1
        else:
            return self.fib(n-2)+self.fib(n-1)"""
        if n==0:
            return prev
        if n==1:
            return curr
        else:
            temp=curr
            curr=curr+prev
            prev=temp
            return self.fib(n-1,prev,curr)



        
