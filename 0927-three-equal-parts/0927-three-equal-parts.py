class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = sum(arr)
        if ones%3!=0: return [-1,-1]
        if ones==0: return [0,2]
        a = ones//3
        n = len(arr)
        p = 0
        while arr[p]==0:
            p+=1
        #p is the first 1 in first segment
        l = n-1
        d = 0
        while d<a:
            d+=arr[l]
            l-=1
        l+=1
        #l is the first 1 in last segment
        h,k = p,l
        #check if first segment equals last segment
        while k<n and arr[h]==arr[k]:
            h+=1
            k+=1
        if k!=n: return [-1,-1]
        s = h
        while arr[s]==0:
            s+=1
        #s is the first 1 in the middle segment
        t = p
        while t<h and arr[t]==arr[s]:
            t+=1
            s+=1
        if t<h: return [-1,-1]
        return [t-1,s]