class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mp1 = dict()
        mp2 = dict()
        for i in range(len(pattern)):
            if pattern[i] not in mp1 and words[i] not in mp2:
                mp1[pattern[i]] = words[i]
                mp2[words[i]] = pattern[i]
            elif pattern[i] in mp1 and words[i] in mp2:
                if mp1[pattern[i]] == words[i] and mp2[words[i]] == pattern[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True