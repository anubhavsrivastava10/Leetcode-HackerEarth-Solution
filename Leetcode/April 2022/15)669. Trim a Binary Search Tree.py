# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > high:
            #trim on the left sub tree
            return self.trimBST(root.left,low,high)
        if root.val <low:
            #trim on the right sub tree
            return self.trimBST(root.right,low,high)
        #if the root is in the range
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root