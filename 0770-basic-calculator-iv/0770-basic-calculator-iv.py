class Vector:
    def __init__(self, base=None, coeff=0):
        self.counter = Counter()
        if base == 1:
            self.counter[1] = coeff
        elif base is not None:
            self.counter[(base,)] = coeff
         
    def add(self, vec):
        for k,v in vec.counter.items():
            self.counter[k] += v
            if self.counter[k] == 0:
                self.counter.pop(k)
    
    def subtract(self, vec):
        for k,v in vec.counter.items():
            self.counter[k] -= v
            if self.counter[k] == 0:
                self.counter.pop(k)
    
    def mergeBase(self, b1, b2):
        if b1 == 1: return b2
        if b2 == 1: return b1
        i = j = 0
        lst = []
        while i < len(b1) and j < len(b2):
            if b1[i] <= b2[j]:
                lst.append(b1[i])
                i += 1
            else:
                lst.append(b2[j])
                j += 1
        if i == len(b1): lst.extend(b2[j:])
        if j == len(b2): lst.extend(b1[i:])    
        return tuple(lst)
    
    def multiply(self, vec):
        counter = Counter()
        for k1, v1 in self.counter.items():
            if v1 == 0: continue
            for k2, v2 in vec.counter.items():
                if v2 == 0: continue
                b = self.mergeBase(k1,k2)
                counter[b] += v1*v2
                if counter[b] == 0:
                    counter.pop(b)
        self.counter = counter
            
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = {v:i for v,i in zip(evalvars, evalints)}
        expression = "("+expression+")"
        vecs = []
        ops = []
        i = 0
        p = None
        while i < len(expression):
            if expression[i] == " ":
                i += 1
                continue
            if expression[i] == "(":
                vecs.append([])
                ops.append([])
                i += 1
            elif expression[i].isalpha():
                j = i+1
                while j < len(expression) and expression[j].isalpha():
                    j += 1    
                vec = Vector(1, int(evalmap[expression[i:j]])) if expression[i:j] in evalmap else Vector(expression[i:j], 1)
                if vecs[-1] == []:
                    vecs[-1].append(vec)
                else:
                    op = ops[-1][-1]
                    if op == "*":
                        ops[-1].pop()
                        vecs[-1][-1].multiply(vec)
                    else:
                        vecs[-1].append(vec)
                i = j
            elif expression[i].isnumeric():
                j = i+1
                while j < len(expression) and expression[j].isnumeric():
                    j += 1
                vec = Vector(1, int(expression[i:j]))
                if vecs[-1] == []:
                    vecs[-1].append(vec)
                else:
                    op = ops[-1][-1]
                    if op == "*":
                        ops[-1].pop()
                        vecs[-1][-1].multiply(vec)
                    else:
                        vecs[-1].append(vec)
                i = j
            elif expression[i] in "+-*":
                ops[-1].append(expression[i])
                i += 1
            elif expression[i] == ")":
                while ops[-1]:
                    vec = vecs[-1].pop()
                    op = ops[-1].pop()
                    if op == "+":
                        vecs[-1][0].add(vec)
                    else:
                        vecs[-1][0].subtract(vec)
                ops.pop()
                vec = vecs.pop()[0]
                if vecs == []: 
                    p = vec
                    break
                if vecs[-1] == []:
                    vecs[-1].append(vec)
                else:
                    op = ops[-1][-1]
                    if op == "*":
                        ops[-1].pop()
                        vecs[-1][-1].multiply(vec)
                    else:
                        vecs[-1].append(vec)
                i += 1
        const = p.counter[1]
        if 1 in p.counter:
            p.counter.pop(1)
        l = [[b,c] for b,c in p.counter.items()]
        l.sort(key=lambda x:(-len(x[0]), x[0]))
        ans = ["*".join([str(c)]+list(b)) for b,c in l]
        if const: ans.append(str(const))
        return ans      