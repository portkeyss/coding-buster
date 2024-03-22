# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = slow = head
        while True:
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        