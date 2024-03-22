class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if nums1 == [0] and nums2 == [0]:
            return [0]
        m, n = len(nums1), len(nums2)
        
        def findLargest(num, p):
            res = []
            idx = -1
            start = 0
            while p > 0:
                for i in range(start, len(num)-p+1):
                    if idx<0  or num[i] > num[idx]:
                        idx = i
                res.append(num[idx])
                start = idx+1
                idx = -1
                p -= 1
            return res
        
        def merge(l1, l2):
            a, b = len(l1), len(l2)
            i = j = 0
            res = []
            while i < a and j < b:
                if l1[i:] < l2[j:]:
                    res.append(l2[j])
                    j += 1
                else:
                    res.append(l1[i])
                    i += 1
            if i < a:
                res.extend(l1[i:])
            if j < b:
                res.extend(l2[j:])
            return res
        
        ans = []
        for p in range(max(0, k-n), min(m,k)+1):
            largestNum1 = findLargest(nums1, p)
            largestNum2 = findLargest(nums2, k-p)
            t = merge(largestNum1, largestNum2)
            ans = max(ans, t)
        return ans