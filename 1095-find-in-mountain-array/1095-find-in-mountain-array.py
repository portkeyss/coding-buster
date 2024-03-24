# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findTop():
            l, r = 1, mountain_arr.length()-2
            while l<r:
                mid = (l+r)//2
                if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    l = mid+1
                else:
                    r = mid
            return r
        def findIndex(start, end, target, inc=True):
            l, r = start, end
            while l<r:
                mid = (l+r)//2
                s = mountain_arr.get(mid)
                if  s == target:
                    return mid
                elif inc:
                    if s< target:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    if s < target:
                        r = mid-1
                    else:
                        l = mid+1
            return r if l==r and mountain_arr.get(r)==target else -1
        peakIndex = findTop()
        ans = findIndex(0,peakIndex,target)
        return ans if ans>-1 else findIndex(peakIndex, mountain_arr.length()-1, target, False)            