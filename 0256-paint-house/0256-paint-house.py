class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #using DP, store the most recent min total cost if last house is painted in either of the three colors
        x = y = z = 0
        for cost in costs:
            a = cost[0]+ min(y,z)
            b = cost[1]+ min(x,z)
            c = cost[2]+ min(x,y)
            x,y,z = a,b,c
        return min([x,y,z])
        