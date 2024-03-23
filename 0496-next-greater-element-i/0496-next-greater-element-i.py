class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        idxMap = dict()
        for idx, m in enumerate(nums1):
            idxMap[m] = idx
        stack = [] #non increasing
        for n in nums2:
            while stack and stack[-1] < n:
                m = stack.pop()
                if m in idxMap:
                    res[idxMap[m]] = n
            stack.append(n)
        return res