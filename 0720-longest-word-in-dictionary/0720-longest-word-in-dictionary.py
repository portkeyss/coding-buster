class Solution:
    def longestWord(self, words: List[str]) -> str:
        class Node:
            def __init__(self):
                self.children = [None]*26
        
        res = ""
        words.sort(key=lambda x:(len(x),x))
        head = Node()
        for w in words:
            t = head
            for i, c in enumerate(w):
                idx = ord(c)-ord('a')
                if t.children[idx]:
                    t = t.children[idx]
                elif i < len(w)-1:
                    break
                else:
                    t.children[idx] = Node()
                    if i+1 > len(res):
                        res = w
        return res
        