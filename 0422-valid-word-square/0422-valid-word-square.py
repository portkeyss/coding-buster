class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        m = max(len(w) for w in words)
        if n != m:
            return False
        matrix = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(len(words[i])):
                matrix[i][j] = words[i][j]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] is None and matrix[j][i] is None:
                    continue
                elif matrix[i][j] is not None and matrix[j][i] is not None:
                    if matrix[i][j] == matrix[j][i]:
                        continue
                    else:
                        return False
                else:
                    return False
        return True