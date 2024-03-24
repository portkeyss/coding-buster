class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        a, b = min(s for s,_ in clips), max(e for _,e in clips)
        if a > 0 or b < time: return -1
        dic = dict()
        for s,e in clips:
            if s in dic:
                dic[s] = max(dic[s], e)
            else:
                dic[s] = e

        res = 0
        t = a
        front = 0
        while front<time:
            newFront = 0
            while t <= front:
                if t in dic:
                    newFront = max(newFront, dic[t])
                t += 1
            if newFront <= front: return -1
            res += 1
            front = newFront
        return res