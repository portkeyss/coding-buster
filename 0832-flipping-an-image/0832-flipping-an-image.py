class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m, n = len(image), len(image[0])
        for i in range(m):
            for j in range(n//2):
                t = image[i][j]
                image[i][j] = image[i][n-1-j]
                image[i][n-1-j] = t
        for i in range(m):
            for j in range(n):
                image[i][j] = 1-image[i][j]
        return image