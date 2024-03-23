class Node:
    def __init__(self):
        self.content = ""
        self.children = defaultdict(Node)
        
class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        if path == "/": return list(sorted(self.root.children.keys()))
        path = path[1:].split("/")
        node = self.root
        for p in path:
            node = node.children[p]
        if node.content: return [path[-1]]
        return list(sorted(node.children.keys()))

    def mkdir(self, path: str) -> None:
        if path == "/": return
        path = path[1:].split("/")
        node = self.root
        for p in path:
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath[1:].split("/")
        node = self.root
        for p in path:
            node = node.children[p]
        node.content += content 

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath[1:].split("/")
        node = self.root
        for p in path:
            node = node.children[p]
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)