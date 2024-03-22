class Node:
    def __init__(self,start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
        
class NumArray:

    def __init__(self, nums: List[int]):
        def construct(i,j):
            root = Node(i,j)
            if i==j:
                root.sum = nums[i]
                return root
            m = (i+j)//2
            l = construct(i,m) 
            r = construct(m+1,j)
            root.left = l
            root.right = r
            root.sum = l.sum+r.sum
            return root
        self.root = construct(0, len(nums)-1)
        

    def update(self, index: int, val: int) -> None:
        def u(node, idx, v):
            if node.start==node.end:
                node.sum = v
            else:
                m = (node.start+node.end)//2
                if m>=idx:
                    node.sum = u(node.left, idx, v)+node.right.sum
                else:
                    node.sum = node.left.sum+u(node.right, idx, v)
            return node.sum
        u(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def prefix(index):
            if index==-1: return 0
            node = self.root
            res = self.root.sum
            while node.start<node.end:
                m = (node.start+node.end)//2
                if index<=m:
                    res -= node.right.sum
                    node = node.left
                else:
                    node = node.right
            return res
        return prefix(right)-prefix(left-1)
                
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)