# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []

    def traverse(self):
        while(self.node):
            self.stack.append(self.node)
            self.node = self.node.left
            
    def next(self) -> int:
        self.traverse()
        node = self.stack.pop()
        self.node = node.right
        return node.val

    def hasNext(self) -> bool:
        return self.stack or self.node


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()