# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse_linked_list(head):
            curr=head
            prev=None
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev

        curr=head
        if curr and curr.next and not curr.next.next:
            return curr.val+curr.next.val
        else:
            length=0
            while curr:
                curr=curr.next
                length+=1
            curr=head
            for _ in range(0,length//2):
                curr=curr.next
            
            llist=reverse_linked_list(curr)
            summ=0
            curr=head
            while llist and curr:
                if llist.val+curr.val > summ:
                    summ=llist.val+curr.val
                llist=llist.next
                curr=curr.next
            return summ

        
