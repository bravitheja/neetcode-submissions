# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q:
            if p.val != q.val:
                return False
            left_tree = self.isSameTree(p.left, q.left)
            right_tree = self.isSameTree(p.right, q.right)
            return left_tree and right_tree
        elif p:
            return False
        elif q:
            return False
        else:
            return True
