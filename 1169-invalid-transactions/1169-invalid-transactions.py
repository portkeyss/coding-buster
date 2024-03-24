class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        transByName = defaultdict(lambda:defaultdict(list))
        for i,t in enumerate(transactions):
            arr = t.split(",")
            #print(arr)
            name, time, amt, city = arr[0], int(arr[1]), int(arr[2]), arr[3]
            if amt > 1000:
                invalid.add(i)
            transByName[name][city].append([time,i])
        for p in transByName.values():
            for q in p.values():
                q.sort()
        for p in transByName.values():
            for c1, l1 in p.items():
                for c2, l2 in p.items():
                    if c1 == c2: continue
                    for m in l1:
                        t1 = m[0]
                        w = bisect.bisect(l2,[t1,-1])
                        while w < len(l2) and l2[w][0] <= 60+t1:
                            invalid.add(m[1])
                            invalid.add(l2[w][1])
                            w += 1
        return [transactions[i] for i in invalid]