class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def f(start, length, A):#the function returns player1's optimal score, given the interval [start, start+interval), A is a flag denoting whether the current player is player1
            if length==0: return 0
            if A:
                return max(nums[start]+f(start+1,length-1,False), f(start,length-1,False)+nums[start+length-1])
            else:
                return min(f(start+1,length-1,True), f(start,length-1,True)) #player2 actively attempts to sabotage player1's effort for more score
        return 2*f(0,len(nums),True)>=sum(nums)