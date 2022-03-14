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
        hm, zero = dict(), Node(0)
        cur, copy = head, zero
        while cur:
            copy.next = Node(cur.val)
            hm[cur] = copy.next
            cur, copy = cur.next, copy.next
        cur, copy = head, zero.next
        while cur:
            copy.random = hm[cur.random] if cur.random else None
            cur, copy = cur.next, copy.next
        return zero.next