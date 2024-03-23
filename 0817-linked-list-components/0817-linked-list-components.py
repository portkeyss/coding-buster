# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        l = head
        nums = set(nums)
        prev = -1
        while l:
            if l.val in nums:
                if prev not in nums:
                    res += 1
            prev = l.val
            l = l.next
        return res  