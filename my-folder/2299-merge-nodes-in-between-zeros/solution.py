# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_sum(prev , curr):
            sum1=0
            while curr.val!=0:
                sum1+=curr.val
                curr=curr.next
            return sum1,prev,curr

        prev=head
        curr=head.next
        
        value,prev,curr=calculate_sum(prev,curr)
        newnode=ListNode(value)
        head=newnode
        prev=curr
        curr=curr.next
        while curr:
            value,prev,curr=calculate_sum(prev,curr)
            newnode.next=ListNode(value)
            newnode=newnode.next
            prev=curr
            curr=curr.next

        return head


        
