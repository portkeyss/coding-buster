class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()
        for b in bills:
            if b==5: counter[5] += 1
            elif b==10:
                if counter[5]==0: return False
                else:
                    counter[5] -= 1
                    counter[10]+=1
            else:
                if counter[10]>0 and counter[5]>0:
                    counter[10] -= 1
                    counter[5] -= 1
                    counter[20] += 1
                elif counter[5]>2:
                    counter[5] -= 3
                    counter[20] += 1
                else:
                    return False
        return True