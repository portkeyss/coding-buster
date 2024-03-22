class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        #build a directed graph for all the numbers a -> list(b), in which b%a = 0 and b > a
        graph = defaultdict(list)
        for i in range(1, len(nums)):
            for j in range(0, i): # the max value of of j should be i-1, because the upper limit of range is exclusive, so upper limit should be i
                if nums[i] % nums[j] == 0:                    
                    graph[nums[j]].append(nums[i])
                  
        dp = dict()            
        def findLongestPath(n: int)-> List[int]:
            if n in dp:
                return dp[n]
            if not graph[n]:
                return [n]
            q = []
            for m in graph[n]:
                p = findLongestPath(m)
                if len(p) > len(q):
                    q = p
            res = [n]+q
            dp[n] = res
            return res
        
        # if b % a == 0 and c % b == 0, then c % a == 0
        # the problem is equivalent to finding the longest path in a graph.
        res = []
        for n in nums:
            p = findLongestPath(n)
            if len(p) > len(res):
                res = p          
        return res