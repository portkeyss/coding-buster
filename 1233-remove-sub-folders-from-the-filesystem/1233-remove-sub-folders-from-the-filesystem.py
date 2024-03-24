class TrieNode:
    def __init__(self, _val, _isEnd):
        self.val = _val
        self.isEnd = _isEnd
        self.desc = dict()
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode("", False)
        for p in folder:
            l = p.split("/")
            node = root
            for x in l[1:]:
                if x not in node.desc:
                    node.desc[x] = TrieNode(x,False)
                node = node.desc[x]
            node.isEnd = True
        res = []
        buffer = []
        stack = []
        stack.append(iter([root]))
        buffer.append(None)
        while stack:
            nxt = next(stack[-1], None)
            if nxt is None:
                stack.pop()
                buffer.pop()
                continue
            buffer[-1] = nxt.val
            if nxt.isEnd:
                res.append("/".join(buffer))
            else:
                stack.append(iter(nxt.desc.values()))
                buffer.append(None)
        return res