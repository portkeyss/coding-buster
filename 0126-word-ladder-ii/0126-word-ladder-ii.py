class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        if beginWord not in wordList: wordList.append(beginWord)
        A = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                A[w[:j]+"?"+w[j+1:]].append(w)
        
        q = deque([beginWord])
        dist = defaultdict(lambda:inf)
        dist[beginWord] = 0
        prev = defaultdict(list)
        
        while q:
            x = q.popleft()  
            if x==endWord:break
            for j in range(len(x)):
                for y in A[x[:j]+"?"+x[j+1:]]:
                    if dist[y]==inf:
                        prev[y].append(x)
                        dist[y] = dist[x]+1
                        q.append(y)
                    elif dist[y]==dist[x]+1:
                        prev[y].append(x)
             
        if dist[endWord]==inf: return []
        res = []
        cur = []
        def f(x):
            if x==beginWord:      
                res.append(cur[::-1])
                return
            for y in prev[x]:
                cur.append(y)
                f(y)
                cur.pop()

        cur = [endWord]
        f(endWord)  
        return res