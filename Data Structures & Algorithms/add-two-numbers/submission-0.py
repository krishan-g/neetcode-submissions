# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry = 0

        while l1 and l2:
            combo = l1.val + l2.val + carry
            
            if combo >= 10:
                combo -= 10
                carry = 1
            else:
                carry = 0
            
            tail.next = ListNode(combo)
            tail = tail.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            combo = l1.val + carry

            if combo >= 10:
                combo -= 10
                carry = 1
            else:
                carry = 0

            tail.next = ListNode(combo)
            tail = tail.next

            l1 = l1.next
        

        while l2:
            combo = l2.val + carry

            if combo >= 10:
                combo -= 10
                carry = 1
            else:
                carry = 0

            tail.next = ListNode(combo)
            tail = tail.next

            l2 = l2.next
        
        if carry:
            tail.next = ListNode(1)
        
        return dummy.next
