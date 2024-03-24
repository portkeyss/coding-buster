class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = [int(i) for i in str(k)]
        carry = 0
        ans = []
        while num or k or carry:
            x = carry
            if num: x += num.pop()
            if k: x += k.pop()
            ans += [x%10]
            carry = x//10
        return reversed(ans)