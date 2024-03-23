class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneSet = set(stones)
        dp = dict()
        def jump(cur_pos, prev_step):
            if cur_pos == stones[-1]:
                return True
            if (cur_pos, prev_step) in dp:
                return dp[(cur_pos, prev_step)] 
            steps = range(max(prev_step - 1, 1), prev_step + 2)
            for step in steps:
                if (cur_pos+step) in stoneSet and jump(cur_pos+step, step):
                    dp[(cur_pos, prev_step)] = True
                    return True
            dp[(cur_pos, prev_step)] = False
            return False
        
        return jump(0,0)