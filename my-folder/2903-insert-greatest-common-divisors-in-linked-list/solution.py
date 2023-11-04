# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        
        prev=head
        curr=head.next

        while prev and curr:
            newnode=ListNode(gcd(prev.val,curr.val))
            newnode.next=curr
            prev.next=newnode
            prev=curr
            curr=curr.next
            
        return head
