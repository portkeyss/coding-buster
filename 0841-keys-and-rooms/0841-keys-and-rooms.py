class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)
        while q:
            r = q.popleft()
            for k in rooms[r]:
                if k not in visited:
                    q.append(k)
                    visited.add(k)
        return len(visited)==len(rooms)