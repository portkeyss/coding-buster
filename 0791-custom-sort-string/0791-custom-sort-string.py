class Solution:
    def customSortString(self, order: str, s: str) -> str:
        seq = {c:i for i,c in enumerate(order)}
        return "".join(sorted(list(s), key=lambda x:seq[x] if x in seq else -1))