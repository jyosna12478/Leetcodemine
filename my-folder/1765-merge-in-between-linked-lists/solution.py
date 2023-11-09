# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1=list2
        prev1=list2
        curr2=list1
        prev2=list1

        while prev1.next is not None:
            prev1=prev1.next

        for i in range(b):
            curr2=curr2.next
        for i in range(a-1):
            prev2=prev2.next

        prev2.next =list2
        prev1.next = curr2.next

        return list1



        


        
