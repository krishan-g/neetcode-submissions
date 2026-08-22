"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        copies = {} # Maps original node to copied node
        
        while curr:

            if curr not in copies:
                curr_copy = Node(curr.val)
                copies[curr] = curr_copy
            else:
                curr_copy = copies[curr]

            if curr.next:
                if curr.next not in copies:
                    next_copy = Node(curr.next.val)
                    copies[curr.next] = next_copy
                curr_copy.next = copies[curr.next]
            
            if curr.random:
                if curr.random not in copies:
                    random_copy = Node(curr.random.val)
                    copies[curr.random] = random_copy
                curr_copy.random = copies[curr.random]
            
            curr = curr.next
        
        return copies.get(head, None)

                
