# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        l = head
        while l:
            l = l.next
            n += 1
        m = n // 2 + 1
        k = 1
        l = head
        while k < m:
            l = l.next
            k += 1
        return l