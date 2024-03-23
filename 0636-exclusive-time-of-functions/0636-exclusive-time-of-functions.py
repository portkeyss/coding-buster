class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        funcStack = []
        startTimeStack = []
        ans = [0]*n
        for log in logs:
            tmp = log.split(':')
            func = int(tmp[0])
            time = int(tmp[2])
            if tmp[1] == 'start':      
                funcStack.append(func)
                startTimeStack.append(time)
            else:
                taskDuration = time + 1 - startTimeStack.pop() # duration from start to end, including waiting time when cpu is executing other tasks
                ans[funcStack.pop()] += taskDuration
                if len(funcStack) !=  0:
                    ans[funcStack[-1]] -= taskDuration #subtract waiting time of the lower stack function when the top stack function shades on the lower stack function          
        return ans