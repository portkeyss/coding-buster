class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        A = [nums[i]-nums[i-1] for i in range(1,len(nums))]  
        prefix = [0]
        x = 0
        for a in A:
            x += a
            prefix.append(x)

        l = min(A)
        r = prefix[-1]
        while l<r:
            mid = (l+r)//2
            count = 0
            for i in range(len(prefix)):
                j = bisect.bisect_right(prefix,mid+prefix[i])
                count += j-i-1
            if count<k: 
                l = mid+1
            elif count>=k:
                r = mid
        return l