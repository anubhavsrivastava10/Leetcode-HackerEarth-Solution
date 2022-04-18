# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        self.s += root.val
        root.val = self.s
        self.dfs(root.left)
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        self.dfs(root)
        return root