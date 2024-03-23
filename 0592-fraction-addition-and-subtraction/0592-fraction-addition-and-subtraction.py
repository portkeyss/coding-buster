class Solution:
    def fractionAddition(self, expression: str) -> str: 
        def add_two_fractions(a,b,c,d):#a/b + c/d
            m = a * d + c * b
            n = b * d
            gcd = math.gcd(m,n)
            return m//gcd, n//gcd
        
        ab = [0,1] # initialize [a,b] to be constructed
        
        i = 0
        while i < len(expression):
            j = i+1
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            l = expression[i:j].split("/")
            c = int(l[0])
            d = 1 if len(l) == 1 else int(l[1])
            ab[0], ab[1] = add_two_fractions(ab[0], ab[1], c, d)
            i = j
            
        res = ""
        if ab[0] < 0:
            res += "-"
        res += str(abs(ab[0])) + "/" + str(ab[1])
        return res
        