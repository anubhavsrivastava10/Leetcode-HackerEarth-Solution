# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if k==0:
            return head
        count = 0
        curr = head
        a = []
        while curr:
            count+=1
            a.append(curr.val)
            curr = curr.next
        # print(count)
        if k==count:
            return head
        k = k%count
        # print(k)
        dummy = ListNode(0)
        curr = dummy
        for i in range(count-k,count):
            curr.next = ListNode(a[i])
            curr = curr.next
        for i in range(0,count-k):
            curr.next = ListNode(a[i])
            curr = curr.next
        return dummy.next