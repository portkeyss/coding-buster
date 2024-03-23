class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def f(x):
            res = 0
            cur = 0 # cur is the number subarrays ending at current index that has max<=x
            for num in nums:
                cur = cur+1 if num<=x else 0
                res += cur
            return res
        return f(right)-f(left-1)