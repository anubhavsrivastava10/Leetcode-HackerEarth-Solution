# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            head.next=self.insertionSortList(head.next)
            d=ListNode(None)
            d.next=head
            v=head.val
            while head.next and head.next.val<v:
                head=head.next
            tmp=head.next
            head.next=ListNode(v)
            head.next.next=tmp
            return d.next.next