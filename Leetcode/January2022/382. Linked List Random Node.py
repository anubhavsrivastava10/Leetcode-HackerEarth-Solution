# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        ans = 0
        p, i = self.head, 0
        while p:
            if random.randint(0, i) == 0: 
                ans = p.val
            p = p.next
            i += 1
        return ans
