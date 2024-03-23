# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        q = deque()
        carry = 0
        i = 0
        while stack1 or stack2 or carry != 0:
            d1 = stack1.pop() if stack1 else 0
            d2 = stack2.pop() if stack2 else 0
            a = carry + d1 + d2
            q.append(a % 10)
            carry = a // 10
        
        node = nextNode = None
        while q:
            node = ListNode(q.popleft(), nextNode)
            nextNode = node
        
        return node
        
            