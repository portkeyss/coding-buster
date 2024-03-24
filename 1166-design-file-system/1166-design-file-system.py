class FileSystem:

    def __init__(self):
        self.Tree = lambda x: (x, dict()) #define a Tree data structure
        self.tree = self.Tree("")

    def createPath(self, path: str, value: int) -> bool:
        path = path[1:].split("/")
        t = self.tree
        for d in path[:-1]:
            if d in t[1]:
                t = t[1][d]
            else:
                return False
        d = path[-1]
        if d in t[1]: return False
        else:
            t[1][d] = self.Tree(value)
            return True
                              

    def get(self, path: str) -> int:
        path = path[1:].split("/")
        t = self.tree
        for d in path[:-1]:
            if d in t[1]:
                t = t[1][d]
            else:
                return -1
        d = path[-1]
        if d in t[1]: return t[1][d][0]
        else:
            return -1
            


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)