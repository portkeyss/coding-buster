class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        heights = [200] + heights + [200]
        n = len(heights)
        K += 1
        while V > 0:
            pos = None
            k = K-1
            while k >= 0:
                if heights[k] < heights[k+1]:
                    pos = k
                elif heights[k] > heights[k+1]:
                    if pos is not None:
                        heights[pos] += 1
                    break
                k -= 1
            if pos is None:
                k = K+1
                while k < n:
                    if heights[k] < heights[k-1]:
                        pos = k
                    elif heights[k] > heights[k-1]:
                        if pos is not None:
                            heights[pos] += 1
                        break
                    k += 1
            if pos is None:
                heights[K] += 1
            V -= 1
        return heights[1:n-1]      