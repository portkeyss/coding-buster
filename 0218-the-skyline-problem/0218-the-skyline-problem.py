from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        A = SortedList()
        points = set()
        start = defaultdict(list)
        end = defaultdict(list)
        for i,(l,r,_) in enumerate(buildings):
            start[l].append(i)
            end[r].append(i)
            points.add(l)
            points.add(r)
        points = sorted(list(points))
        cur = 0
        ans = []
        for p in points:
            for i in end[p]:
                A.remove((-buildings[i][2],i))
            for i in start[p]:
                A.add((-buildings[i][2],i))
            t = -A[0][0] if A else 0
            if t!=cur: 
                cur = t
                ans.append([p,cur])
        return ans