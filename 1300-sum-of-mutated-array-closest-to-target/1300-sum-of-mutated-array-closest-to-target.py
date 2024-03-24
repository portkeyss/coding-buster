class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def f(w):
            return sum(min(x,w) for x in arr)
        left, right = 0, max(arr)
        while left<right-1:
            mid = (left+right)//2
            newSum = f(mid)
            if newSum<target:
                left = mid
            elif newSum==target:
                right = mid
            else:
                right = mid
        return left if target-f(left)<=f(right)-target else right