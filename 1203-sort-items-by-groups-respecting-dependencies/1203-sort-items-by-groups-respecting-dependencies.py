class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        neisGroup = defaultdict(list)
        incomingGroup = Counter()
        neisItemByGroup = defaultdict(lambda:defaultdict(list))
        incomingItemByGroup = defaultdict(Counter)
        groups = set()
        elementsByGroup = defaultdict(set)
        for i,lst in enumerate(beforeItems):
            g1 = group[i] if group[i]>-1 else -i-1
            groups.add(g1)
            elementsByGroup[g1].add(i)
            for j in lst:
                g2 = group[j] if group[j]>-1 else -j-1
                if g1==g2:
                    neisItemByGroup[g1][j].append(i)
                    incomingItemByGroup[g1][i] += 1
                else:
                    neisGroup[g2].append(g1)
                    incomingGroup[g1] += 1
        
        def findOrder(neis,incoming,elements):
            order = []
            A = [x for x in elements if incoming[x]==0]
            if not A: return []
            q = deque(A)
            while q:
                x = q.popleft()
                order.append(x)
                for y in neis[x]:
                    incoming[y] -= 1
                    if incoming[y]==0: q.append(y)
            if len(order)<len(elements): return []
            return order
        
        res = []
        groupOrder = findOrder(neisGroup,incomingGroup,groups)
        if not groupOrder: return []
        for g in groupOrder:
            itemOrder = findOrder(neisItemByGroup[g],incomingItemByGroup[g],elementsByGroup[g])
            if not itemOrder: return []
            res += itemOrder
        return res