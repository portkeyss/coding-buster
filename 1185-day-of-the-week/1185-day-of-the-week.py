class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isLeapYear(y):
            return y%400==0 or y%4==0 and y%100!=0
        
        d0 = 1
        m0 = 1
        y0 = 1971
        w0 = 5
        monthLengthNormal = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        d = w0
        for y in range(y0,year):
            d += 365
            if isLeapYear(y): d += 1
        for m in range(m0, month):
            d += monthLengthNormal[m-1]
            if m==2 and isLeapYear(year): d += 1
        d += day-1
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][d%7]