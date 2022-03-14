# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = ListNode(None)
        dup.next = head
        start = dup
        while start:
            check = False
            while start.next and start.next.next and start.next.val == start.next.next.val:
                start.next = start.next.next
                check = True
            if check:
                start.next = start.next.next
            else:
                start = start.next
        return dup.next