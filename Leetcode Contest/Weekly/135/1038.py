# 1038. Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right: self.bstToGst(root.right)
        root.val = self.curr = self.curr + root.val
        if root.left: self.bstToGst(root.left)
        
        return root
