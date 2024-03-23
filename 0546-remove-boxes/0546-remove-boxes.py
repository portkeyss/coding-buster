class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        
        @lru_cache(None)
        def f(l,r,k):
            if l>r:
                return 0
            j = r
            while j>=l and boxes[j]==boxes[r]:
                j -= 1
                k += 1
            ans = f(l,j,0)+k**2
            for i in range(j-1,l-1,-1):
                if boxes[i]==boxes[r]:
                    ans = max(ans, f(l,i,k)+f(i+1,j,0))
            return ans

        return f(0,n-1,0)