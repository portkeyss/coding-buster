class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        counter = list(sorted([n,freq] for n,freq in counter.items()))
        i = 0
        while i < len(counter):
            if counter[i][1] == 0: 
                i += 1
                continue
            n, freq = counter[i][0], counter[i][1]
            j = 0
            while j < k and i+j < len(counter) and counter[i+j][0] == n+j and counter[i+j][1] >= freq:
                counter[i+j][1] -= freq
                j += 1
            if j < k:
                return False
        return True