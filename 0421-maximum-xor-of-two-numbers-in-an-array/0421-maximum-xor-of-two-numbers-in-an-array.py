class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m = len(bin(max(nums)))-2
        ans = 0
        for i in range(m)[::-1]:
            ans <<= 1
            x = ans+1
            prefix = set(num>>i for num in nums)
            flag = False
            for p in prefix:
                if x^p in prefix:
                    flag = True
                    break
            if flag: ans = x
        return ans