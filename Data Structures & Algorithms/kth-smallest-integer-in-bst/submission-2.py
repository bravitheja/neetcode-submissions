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
        count = 0
        answer = None
        def inOrderTraversal(root):
            nonlocal count
            nonlocal answer
            if not root or answer is not None:
                return            
            
            inOrderTraversal(root.left)


            count+=1
            if count==k:
                answer = root.val
                return
            
            if answer is not None:
                return
            
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        return answer

