class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = 0
        i = 0
        while i<len(arr):
            if arr[i]==0: length += 2
            else: length += 1
            if length>=len(arr): break
            i += 1
        
        j = length-1 #length could be len(arr) or len(arr)+1
        while i>=0:
            if arr[i]==0:
                if j<len(arr):
                    arr[j] = arr[j-1] = 0
                else:
                    arr[j-1] = 0
                i -= 1
                j -= 2
            else:
                arr[j] = arr[i]
                i -= 1
                j -= 1