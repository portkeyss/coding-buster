# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None: return [None for _ in range(k)]
        sz = 0
        t = head
        while t:
            sz += 1
            t = t.next
        p = (sz+k-1)//k #unit size of the first parts
        m = sz-k*p+k #length of first part
        
        t = head
        res = []
        
        i = 0
        while t:
            res.append(t)
            unit = p if i<m*p else p-1
            count = 1
            while t and count < unit:
                t = t.next
                count += 1
                i += 1
            s = t.next
            t.next = None
            t = s
            i += 1
        if p==1:
            res.extend([None for _ in range(k-m)])
        return res