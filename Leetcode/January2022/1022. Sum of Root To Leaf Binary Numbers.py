# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def getSum(node, s):
            if node:
                s = s * 2 + node.val
                if not node.left and not node.right:
                    self.result += s
                getSum(node.left, s)
                getSum(node.right, s)
        getSum(root, 0)
        return self.result
