# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        helper = ListNode(next=head)
        prefix = 0
        prefixIdx = {0:helper}
        t = head
        while t:
            prefix += t.val
            if prefix in prefixIdx:
                q = prefix
                s = prefixIdx[prefix].next
                while s != t:
                    q += s.val
                    prefixIdx.pop(q)
                    s = s.next
                prefixIdx[prefix].next = t.next
            else:
                prefixIdx[prefix] = t
            t = t.next
        return helper.next