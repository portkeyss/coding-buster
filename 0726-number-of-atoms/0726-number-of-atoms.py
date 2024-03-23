class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counterStack = [Counter()]
        n = len(formula)
        i = 0
        while i < n:
            if formula[i] == "(":
                counterStack.append(Counter())
                i += 1
            elif formula[i] == ")":
                j = i+1
                while j < n and formula[j].isnumeric():
                    j += 1
                multiple = int(formula[i+1:j]) if j > i+1 else 1
                for element,ct in counterStack[-1].items():
                    counterStack[-2][element] += ct*multiple
                counterStack.pop()
                i = j
            else:
                j = i+1
                while j < n and formula[j].islower():
                    j += 1
                element = formula[i:j]
                k = j
                while k < n and formula[k].isnumeric():
                    k += 1
                ct = int(formula[j:k]) if k > j else 1
                counterStack[-1][element] += ct
                i = k
        countList = [[element, str(count)] if count > 1 else [element] for element,count in counterStack.pop().items()]
        countList.sort()
        buffer = [a for l in countList for a in l]
        return "".join(buffer)      