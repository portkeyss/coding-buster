class Solution:
    def numberToWords(self, num: int) -> str:
        num = str(num)
        n = len(num)
        if num == "0": return "Zero"
        oneDigit = {"1":"One", "2": "Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
        tensDigit = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen", "18":"Eighteen", "19":"Nineteen"}
        twoDigit = {"2": "Twenty", "3":"Thirty", "4":"Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}
        def f2(m):
            if m < "20": return [tensDigit[m]]
            else:
                if m[1] == "0": return [twoDigit[m[0]]]
                else:
                    return [twoDigit[m[0]], oneDigit[m[1]]]
        def f3(m):
            if m[1:] == "00":
                return  [oneDigit[m[0]], "Hundred"]
            if m[1] == "0":
                return [oneDigit[m[0]], "Hundred"] + [oneDigit[m[2]]]
            return [oneDigit[m[0]], "Hundred"] + f2(m[1:])
        
        def f3_generic(m):
            #trim front zeros
            i = 0
            while i < len(m) and m[i] == "0":
                i += 1
            m = m[i:]
            if m == "": return []
            if len(m) == 1: return [oneDigit[m]]
            if len(m) == 2: return f2(m)
            return f3(m)
        
        buffer = []                                
        if n == 1: buffer = [oneDigit[num]]
        elif n == 2:
            buffer = f2(num)
        elif n == 3:
            buffer = f3(num)
        elif 4 <= n <= 6:
            buffer = f3_generic(num[:-3]) + ["Thousand"] + f3_generic(num[-3:])
        elif 7 <= n <= 9:
            thousands = f3_generic(num[-6:-3])
            if thousands:
                thousands += ["Thousand"]
            buffer = f3_generic(num[:-6]) + ["Million"] + thousands + f3_generic(num[-3:])
        else:
            thousands = f3_generic(num[-6:-3])
            if thousands:
                thousands += ["Thousand"]
            millions = f3_generic(num[-9:-6])
            if millions:
                millions += ["Million"]
            buffer = [oneDigit[num[0]]] + ["Billion"] + millions + thousands + f3_generic(num[-3:])
        return " ".join(buffer)