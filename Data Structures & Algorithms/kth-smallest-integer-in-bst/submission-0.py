# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # left, root, right
        ordered = []
        def inOrderTraversal(root):
            if not root:
                return            

            inOrderTraversal(root.left)
            ordered.append(root.val)
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        return ordered[k-1]

