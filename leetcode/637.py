# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        deq = collections.deque([root])
        
        while deq:
            i = len(deq)
            total = 0
            count = 0
            
            while i > 0:
                node = deq.popleft()
                total += node.val
                
                for leaf in (node.left, node.right):
                    if leaf:
                        deq.append(leaf)
                
                i -= 1
                count += 1
            
            res.append(total/count)
​
                
        return res
        
        
