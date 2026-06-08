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
        if not head:
            return None
        new = {}

        curr = head
        while curr:
            new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                new[curr].next = new[curr.next]
            if curr.random:
                new[curr].random = new[curr.random]
            curr = curr.next
            
        return new[head]
