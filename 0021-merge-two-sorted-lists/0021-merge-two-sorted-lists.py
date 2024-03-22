# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: 
            return l2
        if not l2: 
            return l1
        l = l1
        if l1.val > l2.val: 
            l = l2
        prev = ListNode(0)
        while l2: # merge l2 into l1
            if l1 and l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        prev.next = l1
        return l