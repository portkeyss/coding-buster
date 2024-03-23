class Solution:
    def solveEquation(self, equation: str) -> str:
        n = len(equation)
        flag = True
        pos = True
        coeff = 0
        const = 0
        i = 0
        while i<n:
            if equation[i]=="x":
                coeff += 1 if pos else -1
                i += 1
            elif equation[i]=="=":
                flag = False
                pos = False
                i += 1
            elif equation[i]=="+":
                pos = True if flag else False
                i += 1
            elif equation[i]=="-":
                pos = False if flag else True
                i += 1
            else:
                j = i
                p = 0
                while j<n and equation[j].isnumeric():
                    p = 10*p+int(equation[j])
                    j += 1
                if j<n and equation[j]=="x":
                    coeff += p if pos else -p
                    j += 1
                else:
                    const += p if pos else -p
                i = j
                
        if coeff==0:
            if const==0: return "Infinite solutions"
            else: return "No solution"
        else:
            return "x="+str((-const)//coeff)