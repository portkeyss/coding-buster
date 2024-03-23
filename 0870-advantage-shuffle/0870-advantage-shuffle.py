class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #greedy
        n = len(nums1)
        A = defaultdict(list)
        for i,k in enumerate(nums2):
            A[k].append(i)
        nums1.sort()
        nums2.sort()
        
        res = [-1]*n
        i = 0
        freeDispense = []
        for j in range(n):
            while i<n and nums1[i]<=nums2[j]:
                freeDispense.append(nums1[i])
                i += 1
            if i<n:
                res[A[nums2[j]].pop()]=nums1[i]
                i += 1
        for i in range(n):
            if res[i]==-1: res[i] = freeDispense.pop()
        return res