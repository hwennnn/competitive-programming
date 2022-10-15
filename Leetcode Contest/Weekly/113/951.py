# 951. Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def go(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            
            if node1.val != node2.val: return False
            
            l1, r1 = node1.left, node1.right
            l2, r2 = node2.left, node2.right
            c1 = [l1.val if l1 else None, r1.val if r1 else None]
            c2 = [l2.val if l2 else None, r2.val if r2 else None] 
            
            if not (c1 == c2 or c1 == c2[::-1]):
                return False
​
            return (go(node1.left, node2.left) or go(node1.right, node2.left)) and (go(node1.right, node2.right) or go(node1.left, node2.right))
        
        return go(root1, root2)
