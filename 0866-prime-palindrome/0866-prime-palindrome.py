class Solution:
    def primePalindrome(self, n: int) -> int:
        if n==1: return 2
        def isPrime(a):
            for i in range(2,int(sqrt(a))+1):
                if a%i==0: return False
            return True
        length = len(str(n))
        while True:
            h = (length+1)//2
            for k in range(10**(h-1),10**h):
                half = str(k)
                m = half+half[::-1] if length%2==0 else half+half[-2::-1]
                a = int(m)
                if a >= n and isPrime(a):
                    return a
            length += 1