# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
            currLevel = []
            
            for _ in range(n):
                node = queue.popleft()
                currLevel.append(node.val if node else None)
                
                if node:
                    for leaf in (node.left, node.right):
                        queue.append(leaf if leaf else None)
                    
            if currLevel != currLevel[::-1]: return False
        
        return True
