class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        A = defaultdict(list)
        B = defaultdict(list)
        for ob in obstacles:
            A[ob[0]].append(ob[1])
            B[ob[1]].append(ob[0])
        for l in A.values():
            l.sort()
        for l in B.values():
            l.sort()

        direc = 0 #direction = [[0,1], [-1,0],[0,-1],[1,0]]
        square = 0
        x, y = 0, 0
        for command in commands:
            if command == -2:
                direc = (direc + 1) % 4
            elif command == -1:
                direc = (direc + 3) % 4
            else:
                if direc == 0:
                    i = bisect.bisect_left(A[x], y+1)
                    if i < len(A[x]) and A[x][i] <= y + command:
                        y  = A[x][i] - 1
                    else:
                        y += command
                elif direc == 1:
                    i = bisect.bisect(B[y], x-1)
                    if i > 0 and B[y][i-1] >= x - command:
                        x = B[y][i-1] + 1
                    else:
                        x -= command
                elif direc == 2:
                    i = bisect.bisect(A[x], y-1)
                    if i > 0 and A[x][i-1] >= y - command:
                        y  = A[x][i-1] + 1
                    else:
                        y -= command
                else:
                    i = bisect.bisect_left(B[y], x+1)
                    if i < len(B[y]) and B[y][i] <= x + command:
                        x  = B[y][i] - 1
                    else:
                        x += command
                square = max(square, x**2 + y**2)
        return square