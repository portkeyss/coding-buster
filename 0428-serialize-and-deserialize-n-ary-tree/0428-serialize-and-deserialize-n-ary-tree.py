"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None: return ""
        buffer = ["["]
        stack = [iter([root])]
        while stack:
            nxt = next(stack[-1], None)
            if nxt:
                if buffer[-1] != "[":
                    buffer.append(",")
                buffer.append(str(nxt.val))
                if nxt.children:
                    stack.append(iter(nxt.children))
                    buffer.append("[") 
            else:
                stack.pop()
                buffer.append("]")
        return "".join(buffer)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == "": return None
        stack = [Node(children=[])]
        i = 0
        while i < len(data):
            if data[i] == "[":
                i += 1
            elif data[i] in ",]":
                stack.pop()
                i += 1
            else: 
                j = i
                while data[j].isnumeric():
                    j += 1
                node = Node(int(data[i:j]), children=[])
                stack[-1].children.append(node)
                stack.append(node)
                i = j
        return stack[0].children[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))