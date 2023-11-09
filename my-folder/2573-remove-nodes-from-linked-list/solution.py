# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """if not head:
            return None

        stack=[head.val]
        curr=head.next
        while curr:
            if curr.val <= stack[-1]:
                stack.append(curr.val)
            else:
                while stack[-1] < curr.val:
                    stack.pop()
                stack.append(curr.val)
            curr=curr.next
        
        node=ListNode(stack.pop())
        curr=node
        while stack:
            node.next=ListNode(stack.pop())
            node=node.next

        return curr"""
        if not head:
            return None

        stack = [head.val]
        curr = head.next
        while curr:
            if curr.val <= stack[-1]:
                stack.append(curr.val)
            else:
                while stack and stack[-1] < curr.val:
                    stack.pop()
                stack.append(curr.val)
            curr = curr.next

        # Construct the modified linked list
        stack.reverse()
        new_head = ListNode(stack.pop())
        curr = new_head
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next

        return new_head
        
        
        
