class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # if a % k = b % k, then (a - b) % k == 0
        #the idea is to keep cumulativeSum % K for each index, including the -1 index. then iterate thru all indices, and if cumlativeSum % K is the same with a previous stored, then this subarray is counted      
        modofcsum = defaultdict(int) 
        csum = 0 #index -1 cumulative sum
        modofcsum[csum] = 1
        count = 0
        for a in A:
            csum += a
            count += modofcsum[csum % K]
            modofcsum[csum % K] += 1
        return count