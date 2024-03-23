class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        cur = set()
        res = set()
        for i in arr:
            cur = {i|j for j in cur}
            cur.add(i)
            res.update(cur)
        return len(res)