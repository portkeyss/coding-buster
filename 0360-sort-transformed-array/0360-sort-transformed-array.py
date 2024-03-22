class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        def f(x):
            return a*x*x+b*x+c
        res = sorted(map(f,nums))
        return res