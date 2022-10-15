# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node, curr):
            nonlocal res
            
            if not node: return
            
            if not node.left and not node.right:
                res += curr * 2 + node.val
                return
            
            go(node.left, curr * 2 + node.val) 
            go(node.right, curr * 2 + node.val)
        
        go(root, 0)
        
        return res
