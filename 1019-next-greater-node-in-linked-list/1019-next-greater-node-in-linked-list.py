# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        node = head
        idx = 0
        while node:
            while stack and stack[-1][0] < node.val:
                i = stack.pop()[1]
                res[i] = node.val
            stack.append((node.val,idx))
            node = node.next
            idx += 1
            res.append(0)
        return res