class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        A = {}
        for i in range(len(str1)):
            if str1[i] in A and A[str1[i]] != str2[i]:
                return False
            A[str1[i]] = str2[i]
        return len(set(A.values())) < 26