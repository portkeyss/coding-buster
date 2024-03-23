class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        n = len(num)
        if k == n:
            return '0'
        
        stack = []
        i = 0
        count = 0
        while count < k:
            if stack and (i == n or num[i] < stack[-1]):
                stack.pop()
                count += 1
            else:       
                stack.append(num[i])
                i += 1
                    
        res = stack+list(num[i:])              
        #remove leading zeroes
        j = 0
        while j < len(res) and res[j] == '0':
            j += 1
        res = res[j:] if j < len(res) else ['0']

        return ''.join(res)