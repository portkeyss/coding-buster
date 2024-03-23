class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for s in cpdomains:
            l = s.split()
            ct = int(l[0])
            count[l[1]] += ct
            a = l[1].split('.',maxsplit = 1)
            count[a[1]] += ct
            if '.' in a[1]:
                b = a[1].split('.')
                count[b[1]] += ct
        res = []
        for subdomain, ct in count.items():
            res.append(str(ct) + ' ' + subdomain)
        return res