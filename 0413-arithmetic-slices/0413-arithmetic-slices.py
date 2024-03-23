class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3: return 0
        diff = nums[1]-nums[0]
        l = 2
        res = 0
        for i in range(2,n):
            if nums[i]-nums[i-1]==diff:
                l += 1
            else:
                res += (l-1)*(l-2)//2
                diff = nums[i]-nums[i-1]
                l = 2
        if l>2: res += (l-1)*(l-2)//2
        return res