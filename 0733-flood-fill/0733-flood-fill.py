class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        cl = image[sr][sc]
        if cl == newColor:
            return image
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m, n = len(image), len(image[0])
        
        stack = []
        image[sr][sc] = newColor
        stack.append((sr,sc))
        while stack:
            r,c = stack.pop()
            for d in directions:
                if 0 <= r+d[0] < m and 0 <= c+d[1] < n and image[r+d[0]][c+d[1]] == cl:
                    image[r+d[0]][c+d[1]] = newColor
                    stack.append((r+d[0],c+d[1]))
                
        return image