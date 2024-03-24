class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        i = j = 0
        m = len(slots1)
        n = len(slots2)
        while i < m and j < n:
            if slots1[i][0] >= slots2[j][1]:
                j += 1
            elif slots1[i][1] <= slots2[j][0]:
                i += 1
            else:
                a = max(slots1[i][0], slots2[j][0])
                b = min(slots1[i][1], slots2[j][1])
                if a + duration <= b:
                    return [a,a+duration]
                elif slots1[i][1] <= slots2[j][1]:
                    i += 1
                else:
                    j += 1
        return []