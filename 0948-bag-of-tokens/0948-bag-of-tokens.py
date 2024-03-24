class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        res = 0
        score = 0
        while tokens:
            if power-tokens[0]>=0:
                power -= tokens.popleft()
                score += 1
                res = max(res, score)
            elif score>0:
                power += tokens.pop()
                score -= 1
            else:
                break
        return res