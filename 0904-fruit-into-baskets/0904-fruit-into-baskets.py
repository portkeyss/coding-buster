class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #two pointers
        i = 0
        color = Counter()
        res = 0
        for j in range(len(fruits)):
            color[fruits[j]] += 1
            while len(color)>2:
                color[fruits[i]] -= 1
                if color[fruits[i]] == 0:
                    color.pop(fruits[i])
                i += 1
            res = max(res, j-i+1)
        return res