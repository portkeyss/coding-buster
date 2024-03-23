class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        upper=1<<31
        l=len(str(upper))
        n = len(num)
        for i in range(1,min(n,l)):
            if i>1 and num[0]=="0": continue
            if int(num[:i])>=upper: continue
            for j in range(i+1,min(n,i+l)):
                if j-i>1 and num[i]=="0": continue
                if int(num[i:j])>=upper: continue
                t=[int(num[:i]),int(num[i:j])]
                isFibonacci=True
                k = j
                while k<n:
                    a = t[-1]+t[-2]
                    if a>=upper:
                        isFibonacci = False
                        break
                    if num[k:].startswith(str(a)):
                        t.append(a)
                        k += len(str(a))
                    else:
                        isFibonacci = False
                        break
                if isFibonacci:
                    return t
        return []