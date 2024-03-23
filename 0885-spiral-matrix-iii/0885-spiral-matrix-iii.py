class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        count = R*C
        delta = 1
        step = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        r,c = r0, c0
        d = 0
        res = []
        res.append([r0, c0])
        count -= 1
        while count > 0:
            r += directions[d][0]
            c += directions[d][1]
            if 0 <= r < R and 0 <= c < C:
                res.append([r,c])
                count -= 1
            step += 1
            if step == delta: 
                d = (d+1) % 4
                if d in [0,2]:
                    delta += 1
                step = 0     
        return res