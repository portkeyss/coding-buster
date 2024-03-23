class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for mask in range(1<<n):
            prev = -1
            temp = []
            flag = True
            for i in range(n):
                if mask&(1<<i)>0:
                    if prev<0 or nums[i]>=nums[prev]:
                        temp.append(nums[i])
                    else:
                        flag = False
                        break
                    prev = i
            if flag and len(temp)>1:
                res.add(tuple(temp))
        return [list(p) for p in res]
