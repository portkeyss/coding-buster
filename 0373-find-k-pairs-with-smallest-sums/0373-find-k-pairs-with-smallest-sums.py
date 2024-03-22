class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if nums1 == [] or nums2 == []:
            return []
        hq = []
        s = set()
        heapq.heappush(hq, (nums1[0]+nums2[0], 0, 0))
        s.add((0,0))
        ans = []  
        while hq and len(ans) < k:
            _, i, j = heapq.heappop(hq)
            ans.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1,j) not in s:
                heapq.heappush(hq, (nums1[i+1]+nums2[j], i+1, j))
                s.add((i+1,j))
            if j+1 < len(nums2) and (i, j+1) not in s:
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))
                s.add((i,j+1))
        return ans   