class Solution:
    def countArrangement(self, N: int) -> int:
        candidates = [[] for i in range(N+1)]
        for i in range(1, N+1):
            for k in range(1, N+1):
                if i % k == 0 or k % i == 0:
                    candidates[i].append(k)
                    
        self.ct = 0
        stack = []   
              
        def traverse(i):
            if i == N + 1:
                self.ct += 1
                return
            for k in candidates[i]:
                if k not in stack:
                    stack.append(k)
                    traverse(i+1)
                    stack.pop()
                    
        traverse(1)     
        return self.ct
            