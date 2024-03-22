class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        counter1 = Counter()
        counter2 = Counter()
        for c1, c2 in zip(secret, guess):      
            if c1 == c2:
                bulls += 1
            else:
                counter1[c1] += 1
                counter2[c2] += 1
        for c, freq in counter1.items():
            if counter2[c] > 0: cows += min(freq, counter2[c])
        return "".join([str(bulls), "A", str(cows), "B"])