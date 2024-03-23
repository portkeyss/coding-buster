class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        buffer = []
        flip = 1
        for i in range(0, len(s), k):
            end = min(len(s)-1, i+k-1)
            if flip:
                sb = s[end::-1] if i == 0 else s[end:i-1:-1]
            else:
                sb = s[i:end+1]
            buffer.append(sb)
            flip = 1-flip
        return "".join(buffer)