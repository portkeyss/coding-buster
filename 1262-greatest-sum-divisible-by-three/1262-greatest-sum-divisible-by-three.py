class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        div1 = []
        div2 = []
        for n in nums:
            if n % 3 == 1:
                div1.append(n)
            elif n % 3 == 2:
                div2.append(n)
        div1.sort()
        div2.sort()
        sm = sum(nums)
        if sm % 3 == 0:
            return sm
        if sm % 3 == 1:
            return max(sm - div1[0] if div1 else 0, sm - div2[0] - div2[1] if len(div2) >= 2 else 0)
        if sm % 3 == 2:
            return max(sm - div1[0] - div1[1] if len(div1) >= 2 else 0, sm - div2[0] if div2 else 0)