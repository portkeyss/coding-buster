class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t,c = tomatoSlices, cheeseSlices
        if (t-2*c)%2==0 and (t-2*c)//2>=0 and (4*c-t)%2==0 and (4*c-t)//2>=0:
            return [(t-2*c)//2,(4*c-t)//2]
        else:
            return []