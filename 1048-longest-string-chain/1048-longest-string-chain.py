class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l = [set() for _ in range(17)]
        for w in words:
            l[len(w)].add(w)
        
        mp = defaultdict(lambda: 1)
        mx = 1
        for length in range(1, 17):
            if l[length] == [] or l[length] == []:
                continue
            for w in l[length]:
                for i in range(len(w)):
                    prev = w[:i] + w[i+1:]
                    if prev in l[length-1]:
                        mp[w] = max(mp[w], 1 + mp[prev])
                mx = max(mx, mp[w])
        return mx