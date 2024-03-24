class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        #bucket sort
        bucket = [[] for _ in range(2001)]
        for i in range(len(workers)):
            for j in range(len(bikes)):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                bucket[d].append((i,j))
        res = [-1]*len(workers)
        used = set()
        for d in range(2001):
            if bucket[d]:
                for (i,j) in bucket[d]:
                    if res[i] == -1 and j not in used:
                        res[i] = j
                        used.add(j)
        return res   