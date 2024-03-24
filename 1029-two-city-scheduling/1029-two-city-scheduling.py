class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #let's consider the case in which all people go to city B, then if they go to city A, they need to pay additional cost_a - cost_b. since the cost for all people to go to B is fixed. this problem is equivalent to finding minimum total additional cost if half people go to A. If we sort the array according to this additional cost, then we may choose the lowest n additional cost,i.e., these n people go to A and the rest go to B, we solve this problem
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs)//2
        res = 0
        for i in range(n):
            res += costs[i][0] + costs[i+n][1]
        return res