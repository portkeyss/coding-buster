class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = deque()
        self.snake.append([0,0])
        self.width = width
        self.height = height
        self.food = deque(food)
        self.dir = {'U':(-1,0), 'L':(0,-1), 'R':(0,1), 'D': (1,0)}
        self.score = 0
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0].copy()
        head[0] += self.dir[direction][0]
        head[1] += self.dir[direction][1]
        
        if head[0] < 0 or head[0] >= self.height or head[1] < 0 or head[1] >= self.width:
            return -1      
        if self.food and head[0] == self.food[0][0] and head[1] == self.food[0][1]:
            self.snake.appendleft(head)
            self.food.popleft()
            self.score += 1
        else:
            self.snake.pop()
            if self.snake and head in self.snake:
                return -1
            self.snake.appendleft(head)
        return  self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)