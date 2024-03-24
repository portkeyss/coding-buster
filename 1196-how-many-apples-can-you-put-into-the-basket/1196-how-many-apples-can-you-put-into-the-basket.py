class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        n = 0
        s = 0
        while n < len(arr) and s + arr[n] <= 5000:
            s += arr[n]
            n += 1
        return n