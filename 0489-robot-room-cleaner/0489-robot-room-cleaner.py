# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(row, col, d):
            robot.clean()
            rotate = 0
            while rotate < 4:
                direction = directions[d]
                if (row+direction[0], col+direction[1]) not in visited:
                    if robot.move():
                        visited.add((row+direction[0], col+direction[1]))
                        dfs(row+direction[0], col+direction[1], d)
                        #the following 5 lines is effectively backtracking the robot to the current row, col and direction    
                        robot.turnLeft()
                        robot.turnLeft()
                        robot.move()
                        robot.turnLeft()
                        robot.turnLeft()
                
                robot.turnLeft()
                d = (d+1)%4
                rotate += 1
                 
        visited.add((0,0))
        dfs(0,0,0)   