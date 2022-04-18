# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.curr = TreeNode()
        
        def inorder(node):
            if node:
                inorder(node.left)
                self.curr.right = TreeNode(node.val)
                self.curr = self.curr.right
                inorder(node.right)
        inorder(root)
        return ans.right