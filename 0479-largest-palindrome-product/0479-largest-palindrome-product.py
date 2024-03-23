class Solution:
    def largestPalindrome(self, n: int) -> int:
        def f(even):
            for leftHalf in range(10**n-1, 10**(n-1)-1, -1):
                leftHalf = str(leftHalf)
                x = int(leftHalf+leftHalf[::-1]) if even else int(leftHalf[:]+leftHalf[:-1:-1])
                a = max(10**(n-1), ceil(sqrt(x)), ceil(x/(10**n-1)))
                b = min(10**n-1, x//(10**(n-1)))
                for y in range(a, b+1):
                    if x % y == 0:
                        return x%1337
            return 0
        ans = f(True)
        return ans if ans else f(False)