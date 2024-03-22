# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        lA = headA
        while lA:
            lenA += 1
            lA = lA.next
        lB = headB
        while lB:
            lenB += 1
            lB = lB.next
        lA = headA
        lB = headB
        while lenA < lenB:
            lB = lB.next
            lenB -= 1
        while lenA > lenB:
            lA = lA.next
            lenA -= 1
        while lA and lA != lB:
            lA = lA.next
            lB = lB.next
        return lA
        
            
        
        