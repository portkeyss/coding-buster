class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {"R":[1,0], "L":[-1,0], "U":[0,1], "D":[0,-1]}
        d = [0,0]
        for move in moves:
            d[0] += direction[move][0]
            d[1] += direction[move][1]
        return d[0] == 0 and d[1] == 0