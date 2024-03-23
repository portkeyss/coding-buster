class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mi = math.inf
        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append([num,mi])
            mi = min(num, mi)
        return False