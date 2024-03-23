class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        A = sum(machines)
        if A%n!=0: return -1
        a = A//n
        left = 0
        prev_right = 0
        res = 0
        for x in machines:
            left += x-a
            if left>0 and prev_right>0:
                res = max(res,left+prev_right)    
            else:
                res = max(res,max(abs(left),abs(prev_right)))  
            prev_right = -left
        return res