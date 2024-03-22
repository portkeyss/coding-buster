class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        if n == 0:
            return []
        if n == 1:
            return num if num[0] == target else []
        
        ops = ["", "+", "-", "*"]
        opStack = []
        res = []
        def cal(numList, opList):
            s = []
            s.append(numList[0])
            for i in range(n-1):
                s.append(opList[i])
                s.append(numList[i+1])
            s = "".join(s)
            prevOpIndex = -1
            A = [] #A is numbers list
            B = [] #B is operators list
            for i,c in enumerate(s):
                if c in ["", "+", "-", "*"]:
                    p = s[prevOpIndex+1:i]
                    if len(p)>1 and p[0] == "0":
                        return target+1, [] #ensured to be invalid
                    A.append(int(p))
                    B.append(c)
                    prevOpIndex = i
            p = s[prevOpIndex+1:]
            if len(p)>1 and p[0] == "0":
                return target+1, [] #ensured to be invalid
            A.append(int(p))
            C = deque() #number queue after all products are done
            D = deque() #operators deque after all products are done
            C.append(A[0])
            for i in range(len(B)):
                if B[i] == "*":
                    C[-1] *= A[i+1]
                else:
                    C.append(A[i+1])
                    D.append(B[i])
            ans = C.popleft()
            while D:
                op = D.popleft()
                if op == "+":
                    ans += C.popleft()
                else:
                    ans -= C.popleft()
            return ans,s
        def f():
            if len(opStack) == n-1:
                t, s = cal(num, opStack)
                if t == target:
                    res.append(s)
                return
            for op in ops:
                opStack.append(op)
                f()
                opStack.pop()
        f()
        return res