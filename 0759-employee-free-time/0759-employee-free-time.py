"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        A = {} #dictionary that maps a start time to its largest end time
        for employeeTime in schedule:
            for interval in employeeTime:
                if interval.start not in A or A[interval.start] < interval.end:
                    A[interval.start] = interval.end
        B = [[s,e] for s,e in A.items()]
        B.sort(key=lambda x:x[0])
        res = []
        prevEnd = -1
        for b in B:
            if 0 <= prevEnd < b[0]:
                res.append(Interval(prevEnd,b[0]))
            if b[1] > prevEnd:
                prevEnd = b[1]
        return res