class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n-1
        pair = 0
        while i < j:
            if people[i]+people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
                pair += 1
        return n - pair