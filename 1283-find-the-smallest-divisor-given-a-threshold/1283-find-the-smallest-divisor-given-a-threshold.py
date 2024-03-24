class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mx = max(nums)
        mi = 1
        while mi < mx:
            m = mi + (mx - mi)//2
            if sum([ceil(n/m) for n in nums]) <= threshold:
                    mx = m
            else:
                mi = m + 1
        return mi
        
        