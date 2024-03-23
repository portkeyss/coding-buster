class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if the first digit is not the largest digit, then if we swap it with the largest digit to its right, it becomes largest. if the second digit is not the largest digit starting from itself, then swap it with largest digit to its right.
        # to this end, we need to iterate from right to left. marking the rightmost largest digit and its index so far on the right of the current index(including current index)
        A = map(int, str(num))
        maxDigIdxOnRight = {}
        maxDigIdxOnRight[len(A)-1] = len(A) - 1
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[maxDigIdxOnRight[i+1]]:
                maxDigIdxOnRight[i] = i
            else:
                maxDigIdxOnRight[i] = maxDigIdxOnRight[i+1]
        for i in range(len(A)-1):
            if A[i] < A[maxDigIdxOnRight[i+1]]:
                A[i], A[maxDigIdxOnRight[i+1]] = A[maxDigIdxOnRight[i+1]], A[i]
                return int(''.join(map(str, A)))
        return num
        