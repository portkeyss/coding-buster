class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n < 2: return n
        
        ps = sorted(zip(position,speed))
        times = [(target-x[0])/x[1] for x in ps]
        
        ans = 0
        for i in range(n-1,0, -1):
            if times[i-1] <= times[i]:
                times[i-1] = times[i]
            else:
                ans += 1
        return ans+1