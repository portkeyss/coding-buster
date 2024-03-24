class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        z = list(zip(timestamp,username,website))
        z.sort()       
        d = defaultdict(list)
        for x in z:
            d[x[1]].append(x[2]) #map a user to all websites visited, in time ascending order
        
        m = defaultdict(set) #map a user to its all 3-sequence
        for user, websites in d.items():
            for i in range(len(websites)-2):
                for j in range(i+1, len(websites)-1):
                    for k in range(j+1, len(websites)):
                        m[user].add((websites[i], websites[j], websites[k]))
           
        
        count = collections.Counter()
        for sequences in m.values():
            for sequence in sequences:
                count[sequence] += 1
        p = [w for w in count.keys()]
        p.sort(key = lambda w : (-count[w], w))
        return p[0]