# 968. Binary Tree Cameras
# https://leetcode.com/problems/binary-tree-cameras/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 2
            
            left, right = go(node.left), go(node.right)
            
            if left == 0 or right == 0:
                res += 1
                return 1
            
            return 2 if left == 1 or right == 1 else 0
        
        return (go(root) == 0) + res
