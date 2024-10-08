# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        

        if head is None:
            return None
        
        else:
            curr=head
            prev=None
            while curr:
                if curr.val==val and curr==head:
                    head=head.next
                elif curr.val==val:
                    prev.next=curr.next
                else:
                    prev=curr
                curr=curr.next
            return head




