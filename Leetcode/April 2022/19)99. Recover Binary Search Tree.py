# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = TreeNode(-float('inf'))
        self.curr = None
        self.next = None
        
    def inorder(self, root):
        if not root:
            return
        #move to the left
        self.inorder(root.left)
        
        #check the condition
        if not self.curr and (root.val < self.prev.val):
            self.curr = self.prev
        if self.curr and (root.val < self.prev.val):
            self.next = root
            
        self.prev = root
        self.inorder(root.right)
        
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        
        if not self.curr or not self.next:
            return 
        self.curr.val, self.next.val = self.next.val, self.curr.val
        return