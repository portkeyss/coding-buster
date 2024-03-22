# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        fast = slow = head
        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return head