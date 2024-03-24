class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = defaultdict(lambda:"")
        for region in regions:
            a = region[0]
            for b in region[1:]:
                parent[b]=a
        x, y = region1, region2
        l1 = []
        l2 = []
        while x!="":
            l1.append(x)
            x = parent[x]
        while y!="":
            l2.append(y)
            y = parent[y]
        z = None
        while l1 and l2 and l1[-1]==l2[-1]:
            z = l1[-1]
            l1.pop()
            l2.pop()
        return z