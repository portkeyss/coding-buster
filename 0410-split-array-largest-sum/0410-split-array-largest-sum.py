class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        h = sum(nums)
        while l < h:
            x = (l+h)//2
            s = 0
            ct = 1
            for n in nums:
                if s+n > x:
                    s = n
                    ct += 1
                    if ct > m: break
                else:
                    s += n
            if ct > m: l = x+1
            else:
                h = x
        return h