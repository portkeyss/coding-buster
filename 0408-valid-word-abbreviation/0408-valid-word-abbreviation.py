class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m,n = len(word), len(abbr)
        i = j = 0
        while i<m and j<n:
            if abbr[j].isalpha():
                if word[i]==abbr[j]:
                    i += 1
                    j += 1
                    continue
                else:
                    return False
            else:
                if abbr[j]=="0": return False
                k = j
                while k<n and abbr[k].isnumeric():
                    k += 1
                freq = int(abbr[j:k])
                i += freq
                j = k
        return i==m and j==n