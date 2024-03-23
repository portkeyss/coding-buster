class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        n = len(s)
        diff = []
        for i in range(n):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff)==0:return max(Counter(s).values())>1
        if len(diff)!=2: return False
        return s[diff[0]]==goal[diff[1]] and s[diff[1]]==goal[diff[0]]