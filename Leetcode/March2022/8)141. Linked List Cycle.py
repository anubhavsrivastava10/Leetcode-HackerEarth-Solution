# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        temp = head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False