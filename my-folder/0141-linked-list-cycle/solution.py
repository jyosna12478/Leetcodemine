# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """prev=None
        curr=head
        curr2=head
        while curr:
            temp=curr.next
            curr.next=prev
            if curr.next and prev and curr.next.val==prev.val and prev!=head :
                return True
            prev=curr
            curr=temp
        return False"""
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move one step at a time
            fast = fast.next.next  # Move two steps at a time

            if slow == fast:
                return True  # If there's a cycle, slow and fast will meet

        return False 

        
