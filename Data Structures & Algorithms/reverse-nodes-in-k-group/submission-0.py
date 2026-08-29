# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Get k_th node
            k_node = group_prev
            for _ in range(k):
                if k_node:
                    k_node = k_node.next
            
            if not k_node:
                break
            
            prev, curr = k_node.next, group_prev.next

            group_next = k_node.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            next_prev = group_prev.next
            group_prev.next = k_node
            group_prev = next_prev
        
        return dummy.next
