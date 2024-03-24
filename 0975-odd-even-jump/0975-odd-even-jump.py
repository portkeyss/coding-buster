from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        sl1 = SortedList()
        sl2 = SortedList()
        n = len(arr)
        
        n2i = dict()
        up = dict()
        down = dict()
        for i in range(n-1,-1,-1): 
            j = sl1.bisect_left(arr[i])
            if 0<=j<len(sl1): 
                up[i]=n2i[sl1[j]]
            sl1.add(arr[i])
            k = sl2.bisect_left(-arr[i])
            if 0<=k<len(sl2): 
                down[i]=n2i[-sl2[k]] 
            sl2.add(-arr[i])
            n2i[arr[i]] = i
                
        @lru_cache(None)  
        def f(flag,x):#flag==0 even; flag==1 odd
            if x==n-1:
                return 1
            if flag==0:
                return x in up and f(1,up[x])
            return x in down and f(0,down[x])

        return sum(f(0,i) for i in range(n))