class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        reachable = [False]*n
        while q:
            e = q.popleft()
            nxt = [e-arr[e], e+arr[e]]
            for a in nxt:
                if 0<=a<n and not reachable[a]:
                    if arr[a]==0: return True
                    reachable[a] = True
                    q.append(a)
        return False