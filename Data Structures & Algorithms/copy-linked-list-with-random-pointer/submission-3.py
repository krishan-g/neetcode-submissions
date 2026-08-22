class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copies = {None: None}
        
        # Pass 1: Instaniate all node copies in memory
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Wire next and random pointers using direct lookups
        curr = head
        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next
            
        return copies[head]