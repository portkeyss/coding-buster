class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMostKDistinct(p):
            counter = Counter()
            i = j = 0
            res = 0
            distinct = 0
            while j < len(A):
                counter[A[j]] += 1
                if counter[A[j]] == 1:
                    distinct += 1
                while distinct > p:
                    counter[A[i]] -= 1
                    if counter[A[i]] == 0:
                        distinct -= 1
                    i += 1
                res += j-i+1
                j += 1
            return res        
        return atMostKDistinct(K)-atMostKDistinct(K-1)