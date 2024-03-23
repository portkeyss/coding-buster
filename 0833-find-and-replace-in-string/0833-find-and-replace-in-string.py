class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        buffer = []
        T = list(zip(indexes,sources,targets))
        T.sort()
        j = 0
        for i,x,t in T:
            if S[i:].startswith(x):
                buffer.append(S[j:i])
                buffer.append(t)
                j = i+len(x)
        buffer.append(S[j:])
        return "".join(buffer)