class Solution:
    def pathSum(self, nums: List[int]) -> int:
        A = [-1]*((1<<5)-1)
        for num in nums:
            x = [int(c) for c in str(num)]
            d,p,v = x[0],x[1],x[2]
            i = (1<<(d-1))-1+p-1
            A[i] = v

        self.ans = 0
        
        def f(j):
            if j>=(1<<6) or A[j]==-1:
                return 0
            l = f(2*j+1)
            r = f(2*j+2)
            count = l+r
            if count==0:
                count = 1
            self.ans += count*A[j]
            return count

        f(0)
        return self.ans