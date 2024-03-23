class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        ct = [0]*10
        ct[0] = counter["z"]
        ct[2] = counter["w"]
        ct[4] = counter["u"]
        ct[1] = counter["o"]-ct[0]-ct[2]-ct[4]
        ct[5] = counter["f"]-ct[4]
        ct[6] = counter["x"]
        ct[7] = counter["s"]-ct[6]
        ct[8] = counter["g"]
        ct[3] = counter["h"]-ct[8]
        ct[9] = counter["i"]-ct[5]-ct[6]-ct[8]
        return "".join([str(i)*c for i,c in enumerate(ct)])