class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        A = defaultdict(set)
        for e in emails:
            l = e.split("@")
            A[l[1]].add((l[0].split("+"))[0].replace(".",""))
        return sum(len(v) for v in A.values())