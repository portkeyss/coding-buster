class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1: #the rotated minimum
            return min(s[i:]+s[:i] for i in range(0,len(s)))
        else:#minimum of the all permutated(allowing swap of adjacent means allowing for all permutations)
            return "".join(sorted(s))