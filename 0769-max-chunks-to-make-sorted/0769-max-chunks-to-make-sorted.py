class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        res = 0
        while i < n:
            end = i
            j = i
            while j <= end:
                k = n-1
                while k > j and arr[k]>arr[j]:
                    k -= 1
                end = max(end,k)
                j += 1
            res += 1
            i = end+1
        return res      