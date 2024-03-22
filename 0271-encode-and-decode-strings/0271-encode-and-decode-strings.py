class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        buffer = []
        for s in strs:
            buffer.append(chr(len(s))) #turn number from 0 to 255 to ASCII char
            buffer.append(s)
        return "".join(buffer)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            l = ord(s[i])
            res.append(s[i+1:i+1+l])
            i += 1+l
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))