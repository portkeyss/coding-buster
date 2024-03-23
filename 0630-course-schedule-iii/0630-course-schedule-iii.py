class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1]) #sort by end time
        pq = []
        front = 0
        for d,e in courses:
            heapq.heappush(pq,-d)
            front += d
            if front>e: front -= -heapq.heappop(pq)
        return len(pq)