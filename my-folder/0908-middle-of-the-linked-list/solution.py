# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!= None:
            curr=curr.next
            count=count+1
        head1=head
        if count%2==0:
            count=int(count/2)
        else:
            count=int((count-1)/2)
        for _ in range (0,count):
            head1=head1.next
        return head1
