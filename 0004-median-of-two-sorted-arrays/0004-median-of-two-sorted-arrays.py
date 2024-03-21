class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(a1,a2,k):
            if not a1: return a2[k-1]
            if not a2: return a1[k-1]
            if k==1: return min(a1[0],a2[0])
            if len(a1)>len(a2): return kth(a2,a1,k)
            p = min(k,len(a1))
            q = min(k,len(a2))
            l1 = (p-1)//2
            l2 = k-(p-1)//2-2
            if (l2+1==q or a1[l1]<=a2[l2+1]) and (l1+1==p or a2[l2]<=a1[l1+1]):
                return max(a1[l1],a2[l2])
            elif l2+1<q and a1[l1]>a2[l2+1]:
                return kth(a1[:l1],a2,k)
            else:
                return kth(a1[l1+1:],a2,k-l1-1)
        
        m,n = len(nums1), len(nums2)
        if (m+n)%2==0: return 0.5*(kth(nums1,nums2,(m+n)//2)+kth(nums1,nums2,(m+n)//2+1))
        else: return kth(nums1,nums2,(m+n+1)//2)