class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(i,j):
            n1, n2 = num[:i], num[i:j]
            if len(n1) > 1 and n1[0] == "0" or len(n2) > 1 and n2[0] == "0":
                return False
            while j < len(num):
                n3 = str(int(n1)+int(n2))
                if num[j:].startswith(n3):
                    j += len(n3)
                    n1, n2 = n2, n3
                else:
                    return False
            return True
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):          
                if check(i,j):
                    return True
        return False