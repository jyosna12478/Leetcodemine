# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        curr=head
        for _ in range(0,k-1):
            curr=curr.next
        curr2=head
        for _ in range(0,length-k):
            curr2=curr2.next
        temp=curr.val
        curr.val=curr2.val
        curr2.val=temp

        return head


        
