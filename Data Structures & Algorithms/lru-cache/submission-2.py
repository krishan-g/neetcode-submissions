class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {} # maps keys to nodes
        
        self.dummy = ListNode()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
    
    def add(self, node):
        """
        Add node to MRU position (head).
        """
        node.prev = self.dummy
        node.next = self.dummy.next

        self.dummy.next.prev = node
        self.dummy.next = node
    
    def remove(self, node):
        """
        Remove node from position.
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key):
        if key in self.map:
            node = self.map[key]

            self.remove(node)
            self.add(node)

            return node.val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value

            self.remove(node)
            self.add(node)
        else:
            node = self.map[key] = ListNode(key, value)

            self.add(node)

            if len(self.map) > self.capacity:
                del self.map[self.dummy.prev.key]
                self.remove(self.dummy.prev)
