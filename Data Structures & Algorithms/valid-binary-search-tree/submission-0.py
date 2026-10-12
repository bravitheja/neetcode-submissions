# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        

        def isValid(node: TreeNode, low, high):
            
            if not node:
                return True
            
            if low < node.val < high:
                return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
            else:
                return False
        
        return isValid(root, float('-inf'), float('inf'))