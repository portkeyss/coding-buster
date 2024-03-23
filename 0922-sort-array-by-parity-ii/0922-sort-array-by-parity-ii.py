class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        #2 pointers approach. treat the A as two arrays, odd indices array and even indices array. We use two pointers i and j, each increment 2 to iterate thru their respective array. we swap any time when both entries are misplaced.
        i, j = 0, 1
        while i < len(A):
            if A[i] % 2 == 0:
                i += 2
                continue
            while A[j] % 2 != 0:
                j += 2
            A[i], A[j] = A[j], A[i]
        return A