class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        k = 1 # "should-be" candy for the current person
        i = 0 
        res = [0]*num_people
        while candies > k:
            res[i % num_people] += k
            candies -= k
            i += 1
            k += 1
        res[i % num_people] += candies
        return res