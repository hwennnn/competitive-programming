# 1457. Pseudo-Palindromic Paths in a Binary Tree
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def dfs(self, root, mp):
        if not root: return
        
        mp[root.val] += 1
        
        if not root.left and not root.right and sum(v&1 for v in mp.values()) <= 1:
            self.count += 1
        
        self.dfs(root.left, mp)
        self.dfs(root.right, mp)
        
        mp[root.val] -= 1
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.dfs(root, collections.defaultdict(int))
        
        return self.count