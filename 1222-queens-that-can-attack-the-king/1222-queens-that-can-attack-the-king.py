class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        A = [(inf,-1) for _ in range(8)]
        r, c = king[0], king[1]
        for i,(x,y) in enumerate(queens):
            if x==r: 
                if c>y:
                    A[0] = min(A[0],(c-y,i))
                else:
                    A[1] = min(A[1],(y-c,i))
            if y==c: 
                if r>x:
                    A[2] = min(A[2],(r-x,i))
                else:
                    A[3] = min(A[3],(x-r,i))
            if x-y==r-c: 
                if r>x:
                    A[4] = min(A[4],(r-x,i))
                else:
                    A[5] = min(A[5],(x-r,i))
            if x+y==r+c: 
                if r>x:
                    A[6] = min(A[6],(r-x,i))
                else:
                    A[7] = min(A[7],(x-r,i))      
        return [queens[i] for _,i in A if i>-1]