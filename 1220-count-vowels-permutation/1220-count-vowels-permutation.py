class Solution:
    def countVowelPermutation(self, n: int) -> int:
        p = [1,1,1,1,1] # we keep a record of number of strings that ends with a e i o u, for current lengh of string. then we can transfer the numbers of length to the case of length+1 using deduction relation. Since a can be preceeded only by e i u, then all the numbers of old strings that ends with e i u can be summed to get the number for new strings that ends with a. Other characters follows similar pattern. We can assign these numbers in an array of length 5, corresponds to five vowels
        for i in range(2,n+1):
            q = []
            q.append(p[1]+p[2]+p[4])
            q.append(p[0]+p[2])
            q.append(p[1]+p[3])
            q.append(p[2])
            q.append(p[2]+p[3])
            p = q
        return sum(p) % (10**9+7)