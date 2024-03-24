class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        mp = dict() #map index of "(" to its depth and index of its matching ")"
        balance = 0
        depth = 0
        for i,c in enumerate(seq):
            if c == "(":
                balance += 1
                stack.append(i)
                mp[i] = [balance]
                depth = max(depth, balance)
            if c == ")":
                balance -= 1
                mp[stack.pop()].append(i)
        newDepth = depth//2
        res = [0]*len(seq)
        i = 0
        while i < len(seq):
            if seq[i] == "(" and mp[i][0] == newDepth+1:
                j = mp[i][1]
                while i <= j:
                    res[i] = 1
                    i += 1
            else:
                i += 1
        return res