class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        buffer = []
        i = len(arr1)-1
        j = len(arr2)-1
        carry = 0
        while carry or i>=0 or j>=0:
            a = carry
            if i>=0:
                a += arr1[i]
                i -= 1
            if j>=0:
                a += arr2[j]
                j -= 1
            buffer.append(a+2*ceil(a/(-2)))
            carry = ceil(a/(-2))
        while buffer and buffer[-1]==0: buffer.pop()
        if not buffer: buffer.append(0)
        return buffer[::-1]