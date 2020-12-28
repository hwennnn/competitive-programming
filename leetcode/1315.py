# 1315. Sum of Nodes with Even-Valued Grandparent
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperR(self, root, l):
        if not root: return 0
        if l == 0: return root.val
        
        left_c = self.helperR(root.left, l-1) 
        right_c = self.helperR(root.right, l-1)
        
        return left_c + right_c
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return 0
        res = self.helperR(root, 2) if root.val % 2 == 0 else 0

        return res + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
    
    # dfs to the end
    def dfs(self, current, parent, grandparent):
        if not current: return 0
        res = 0
        if grandparent and grandparent.val % 2 == 0:
            res += current.val
        
        return res + self.dfs(current.left, current, parent) + self.dfs(current.right, current, parent)
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, None, None)