class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def number(i):
            if i == 0 or i == 7:
                return 0
            if cells[i-1] == cells[i+1]:
                return 1
            else:
                return 0
        M = {} # Maps string to its index
        P = {} # Maps index to its string
        for i in range(1, N + 1):
            newCells = []
            for k in range(8):
                newCells.append(number(k))
            cells = newCells
            strCells = "".join([str(cell) for cell in cells])
                   
            if strCells in M:                
                j = M[strCells]
                cells = list([int(c) for c in P[j + (N - j) %(i - j)]])
                break
             
            M[strCells] = i
            P[i] = strCells
  
        return cells