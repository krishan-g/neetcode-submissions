# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))
        heapq.heapify(heap)

        while heap:
            value, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            new_node = node.next
            if new_node:
                heapq.heappush(heap, (new_node.val, idx, new_node))
        
        return dummy.next
        
