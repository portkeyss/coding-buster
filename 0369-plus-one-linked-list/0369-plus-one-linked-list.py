# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0,head)
        p = sentinel
        q = p
        while p:
            if p.val != 9: q = p
            p = p.next
        q.val += 1
        q = q.next
        while q:
            q.val = 0
            q = q.next
        return sentinel if sentinel.val == 1 else head