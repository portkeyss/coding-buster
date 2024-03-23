class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #BFS problem
        if target=='0000': return 0
        if '0000' in deadends:
            return -1
        q = deque()
        dist = {}
        q.append('0000')
        dist['0000'] = 0
        for deadend in deadends:
            dist[deadend] = float('inf')
        while q:
            code = q.popleft()
            for i in range(4):
                newDigits =[str((int(code[i])+1) % 10), str((int(code[i])-1) % 10)]
                for newDigit in newDigits:
                    newCode = code[:i]+newDigit+code[i+1:]
                    if newCode not in dist:
                        q.append(newCode)
                        dist[newCode] = dist[code] + 1
                        if newCode == target:
                            return dist[newCode]                   
        return -1