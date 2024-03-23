class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        epsilon = 1e-10
        oneNums = dict()
        twoNums = defaultdict(set)
        threeNums = defaultdict(set)
        for i, n in enumerate(nums):
            oneNums[i] = n
        for i in range(4):
            for j in range(i+1,4):
                twoNums[(i,j)].add(nums[i]+nums[j])
                twoNums[(i,j)].add(nums[i]*nums[j])
                twoNums[(i,j)].add(nums[i]-nums[j])
                twoNums[(i,j)].add(nums[j]-nums[i])
                twoNums[(i,j)].add(nums[i]/nums[j])
                twoNums[(i,j)].add(nums[j]/nums[i])
        for (i,j),s in twoNums.items():
            for k in range(4):
                if k != i and k!= j:
                    for n in s:
                        key = tuple(sorted([i,j,k]))
                        threeNums[key].add(n + nums[k])
                        threeNums[key].add(n * nums[k])
                        threeNums[key].add(n - nums[k])
                        threeNums[key].add(nums[k] - n)
                        threeNums[key].add(n / nums[k])
                        if n != 0:
                            threeNums[key].add(nums[k]/n)
        for (i,j,k),s in threeNums.items():
            for l in range(4):
                if l != i and l!= j and l!= k:
                    for n in s:
                        if abs(n + nums[l] - 24) < epsilon or abs(n * nums[l] - 24) < epsilon or abs(n - nums[l] - 24) < epsilon or abs(nums[l]- n - 24) < epsilon or abs(n / nums[l] - 24) < epsilon or (n != 0 and abs(nums[l]/n - 24) < epsilon):
                            return True
        for (i,j,k,l) in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
            for a in twoNums[(i,j)]:
                for b in twoNums[(k,l)]:
                    if abs(a + b - 24) < epsilon or abs(a * b- 24) < epsilon or abs(a - b - 24) < epsilon or abs(b - a- 24) < epsilon or (b != 0 and abs(a /b - 24) < epsilon) or (a != 0 and abs(b / a - 24) < epsilon):
                        return True
        return False 