class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #the intuition is to build a count for all the possible mod values
        count = collections.Counter()
        for t in time:
            count[t % 60] += 1
          
        tot = 0
        for mod, ct in count.items():
            if mod > 30: # if mod > 30, then possible pairs are already counted in 60 - mod
                continue
            if mod == 0 or mod == 30: # matched pairs stay in the same bucket
                tot += (ct * (ct-1))//2
            else:
                tot += ct * count[60-mod]
        return tot
                
                