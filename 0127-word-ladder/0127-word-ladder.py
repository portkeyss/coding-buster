class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if beginWord not in wordList: wordList.append(beginWord)
        A = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                A[w[:j]+"?"+w[j+1:]].append(w)
        l = [beginWord]
        visited = {beginWord}
        d = 1
        while l:
            t = []
            for x in l:
                for j in range(len(x)):
                    for y in A[x[:j]+"?"+x[j+1:]]:
                        if y not in visited:
                            if y==endWord: return d+1
                            visited.add(y)
                            t.append(y)
            d += 1
            l = t
        return 0