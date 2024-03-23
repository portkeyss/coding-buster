class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] #stack should be in the form of ----+++++
        for a in asteroids:
            if a < 0:
                while stack and 0 < stack[-1] < -a:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == -a:
                    stack.pop()
            else:
                stack.append(a)
        return stack