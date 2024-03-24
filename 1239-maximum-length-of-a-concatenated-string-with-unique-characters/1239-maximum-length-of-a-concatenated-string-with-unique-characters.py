class Solution:
    def maxLength(self, arr: List[str]) -> int:
        C = [0]
        count = 0
        for a in arr:
            m = 0
            for ch in a:
                if 1 << (ord(ch)-ord('a')) & m != 0:
                    m = 0
                    break
                m |= 1 << (ord(ch)-ord('a'))
            if m == 0:
                continue
            
            for comb in C[:]:
                if m & comb != 0:
                    continue
                count = max(count, bin(m|comb).count("1"))
                C.append(m|comb)
        return count