# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = head
        for _ in range(n):
            first = first.next
        
        if not first:
            return head.next
        
        prev, second = None, head

        while first:
            first = first.next
            
            prev = second
            second = second.next
        
        prev.next = second.next
        second.next = None

        return head