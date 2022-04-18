# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        n=0
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
                
            if stack:
                node=stack.pop()
                n+=1
            else:
                break
            
            if n==k:
                return node.val
            
            root=node.right
            