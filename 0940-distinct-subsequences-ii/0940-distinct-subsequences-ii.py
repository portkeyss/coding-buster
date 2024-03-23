class Solution:
    def distinctSubseqII(self, s: str) -> int:
        count = 1 # empty string
        mod = 10**9+7
        end = [0]*26
        for c in s:
            pre = count
            count = ((2*count)%mod-end[ord(c)-ord('a')]+mod)%mod #subtract double counting
            end[ord(c)-ord('a')]=pre
        return (count-1)%mod #subtract empty string