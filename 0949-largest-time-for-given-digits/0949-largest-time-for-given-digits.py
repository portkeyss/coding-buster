class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        dp = defaultdict(list)
        dp[0]=[""]
        latest = ""
        
        def getOnes(p):
            count = 0
            while p:
                p &= p-1
                count += 1
            return count
        
        for mask in range(1,1<<4):
            for j in range(4):
                if (1<<j)&mask:
                    for l in dp[mask^(1<<j)]:
                        dp[mask].append(l+str(arr[j]))
                if getOnes(mask)==4:
                    for l in dp[mask]:
                        hh = l[:2]
                        mm = l[2:]
                        if "00"<=hh<="23" and "00"<=mm<="59":
                            cur = hh+":"+mm
                            if cur>latest: latest=cur
        return latest