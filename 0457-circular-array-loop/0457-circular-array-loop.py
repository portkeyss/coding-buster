class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        helper = 10000
        bound = 1000
        n = len(nums)
        for i in range(n):
            if nums[i] > bound: continue #already visited
            sign = 1 if nums[i] > 0 else -1
            j = i
            while True:              
                if nums[j] == helper:# visited nums in current while loop
                    return True
                if nums[j]*sign < 0:
                    break
                if bound < nums[j] < helper:#visited in the prior for steps
                    break    
                if nums[j]%n == 0:
                    nums[j] = helper
                    break
                nxt = (j+nums[j])%n
                nums[j] = helper
                j = nxt
            helper += 1
        return False