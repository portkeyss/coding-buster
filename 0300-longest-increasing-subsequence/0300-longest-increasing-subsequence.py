class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for a in nums:
            i = bisect.bisect_left(sub,a)
            if i==len(sub):
                sub.append(a)
            else:
                sub[i]=a
        return len(sub)