class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dq = deque()
        count = {}
        ans = 0
        for c in s:
            dq.append(c)
            count[c] = count.get(c, 0) + 1
            while len(count) > k:
                n = dq.popleft()
                if count[n] > 1:
                    count[n] -= 1
                else:
                    count.pop(n)
            ans = max(ans, len(dq))
        return ans