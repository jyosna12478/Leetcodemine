# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        root=head
        curr=head.next

        while curr:
            (root.val,curr.val)=(curr.val,root.val)
            root=curr.next
            if not root:
                break
            curr=root.next

        return head
        
