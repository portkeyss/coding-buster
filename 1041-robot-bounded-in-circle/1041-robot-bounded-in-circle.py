class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0,1], [-1,0], [0,-1],[1,0]]
        
        direction = 0    
        x = y = 0
        
        quadruIns = ""
        for j in range(4):
            quadruIns += instructions
        
        for i in quadruIns:
            if i == 'G':
                x += directions[direction][0]
                y += directions[direction][1]
            elif i == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction + 3) % 4
        
        return x == 0 and y == 0