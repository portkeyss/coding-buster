class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        if x == y == 0:
            return z == 0
        if x == 0:
            return z == 0 or z == y
        if y == 0:
            return z == 0 or z == x
        gcd = math.gcd(x,y)
        return z % gcd == 0