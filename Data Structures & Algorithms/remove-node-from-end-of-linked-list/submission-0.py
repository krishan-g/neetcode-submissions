# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        if count == n:
            new_head = head.next
            head.next = None
            return new_head
        
        prev, curr = None, head
        for i in range(count - n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None

        return head

