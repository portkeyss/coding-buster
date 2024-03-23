# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        #flatten 2-d array to 1-d array
        while True:
            row, col = rand7()-1, rand7()-1 #use 0-based index
            idx = row*7+col 
            if idx<40: return 1+idx%10
            row, col = idx-40, rand7()-1
            idx = row*7+col
            if idx<60: return 1+idx%10
            row, col = idx-60, rand7()-1
            idx = row*7+col
            if idx<20: return 1+idx%10