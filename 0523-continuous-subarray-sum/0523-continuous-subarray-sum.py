class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """        
        # 1.construct cummulative summation list from nums list
        # 2.check if cummulative sum list can contain same sum%k, if it does, then sum between them can be viewed as divisible by k. proof is simple: if a%k = d and b%k = d, then (b-a)%k = d. Note that if k = 0, we write it as a = a + 0 * (any integer), so mod residual is a.
        cumSumList = []
        
        #cummulative sum prior to the first element should be populated as zero
        cumSum = 0
        cumSumList.append(cumSum)
        
        for num in nums:
            cumSum += num
            cumSumList.append(cumSum)

        resMap = {} # map a given residual to its earliest index
        for i in range(len(cumSumList)): 
            res = cumSumList[i] if k == 0 else cumSumList[i] % k
            if res not in resMap:           
                resMap[res] = i
            elif resMap[res] < i - 1: # the subarray must have min size 2
                return True
        return False
                