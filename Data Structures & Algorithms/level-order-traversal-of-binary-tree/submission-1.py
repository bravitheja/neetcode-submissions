# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        result = list()
        result.append([root.val])


        while queue:

            level_length = len(queue)
            level = []
            for _ in range(level_length):
                node = queue.popleft()

                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
            
            if level:
                result.append(level)
        
        return result
