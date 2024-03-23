class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        res = 0
        for c in s:
            if c=="(":
                balance += 1
            else:
                balance -= 1
                if balance == -1:
                    res += 1
                    balance = 0
        if balance > 0:
            res += balance
        return res