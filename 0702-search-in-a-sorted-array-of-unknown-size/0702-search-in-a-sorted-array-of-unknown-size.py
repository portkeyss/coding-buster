# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        def findlength(reader):
            l, r = 0, 10**4
            while l < r:
                mid = (l+r)//2
                if reader.get(mid) < 10**4:
                    l = mid + 1
                else:
                    r = mid
            return r
        
        length = findlength(reader)
        l, r = 0, length-1
        while l < r:
            mid = (l+r)//2
            if reader.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        return r if reader.get(r) == target else -1  