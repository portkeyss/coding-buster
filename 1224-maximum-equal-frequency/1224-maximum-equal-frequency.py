class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        highFreq = 0
        counter = Counter()
        freqCounter = Counter()
        res = 0
        for i,num in enumerate(nums):
            counter[num] += 1
            highFreq = max(highFreq, counter[num])
            if freqCounter[counter[num]-1]>0:
                freqCounter[counter[num]-1]-=1
            freqCounter[counter[num]]+=1
            if highFreq==i+1 or highFreq==1 or highFreq*freqCounter[highFreq]==i or (highFreq-1)*(freqCounter[highFreq-1]+1)==i:
                res = i+1
        return res