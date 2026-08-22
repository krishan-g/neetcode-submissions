# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev = slow
            
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        if slow is head:
            return
            
        other_head = self.reverseList(slow)

        self.mergeList(head, other_head)
  
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def mergeList(self, head, other_head):
        l1 = head
        l2 = other_head

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        
        dummy.next = None