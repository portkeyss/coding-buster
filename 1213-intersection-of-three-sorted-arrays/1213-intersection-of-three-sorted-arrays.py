class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def twoArrayIntersection(A, B):
            i = j = 0
            m, n = len(A), len(B)
            ans = []
            while i < m and j < n:
                if A[i] == B[j]:
                    ans.append(A[i])
                    i += 1
                    j += 1  
                elif A[i] < B[j]:
                    i += 1
                else:
                    j += 1
            return ans
        return twoArrayIntersection(twoArrayIntersection(arr1, arr2), arr3)