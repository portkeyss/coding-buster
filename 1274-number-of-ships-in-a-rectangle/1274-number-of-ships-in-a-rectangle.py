# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def f(a,b,c,d):
            p = sea.hasShips(Point(c,d),Point(a,b))
            if p is False: return 0
            if a==c and b==d: return p
            w = (a+c)//2
            v = (b+d)//2
            if a==c:   
                return f(a,b,a,v)+f(a,v+1,a,d)
            elif b==d:
                return f(a,b,w,b)+f(w+1,b,c,b)
            else:
                return f(a,b,w,v)+f(a,v+1,w,d)+f(w+1,v+1,c,d)+f(w+1,b,c,v)
                
        return f(bottomLeft.x, bottomLeft.y,topRight.x, topRight.y)