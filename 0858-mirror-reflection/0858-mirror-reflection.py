class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        y = p*q//gcd(p,q) #total y distance = least common multiple of p and q
        x = y*p//q # x_speed == y_speed*p//q, therefore x_distance = y_distance*p//q
        m, n = x//p, y//p # number of reflections on x and y axes, resp.
        if m%2==0: return 2 #reflected in y_axis even times
        elif n%2==1: return 1 #reflected in x_axis odd times
        else: return 0 #reflected in x_axis even times