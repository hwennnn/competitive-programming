# 2415. Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        
        dq = deque([root])
        level = 0
        
        while dq:
            n = len(dq)
            curr = []
            
            for _ in range(n):
                node = dq.popleft()
                curr.append(node.val)
                
                for child in filter(None, (node.left, node.right)):
                    dq.append(child)
            
            if level % 2 == 1:
                curr.reverse()
            
            res += curr
            level += 1
            
        n = len(res)
        
        def go(i):
            root = None
            
            if i < n:
                root = TreeNode(res[i]) 
​
                # insert left child 
                root.left = go(2 * i + 1)
​
                # insert right child 
                root.right = go(2 * i + 2)
​
            return root
        
        return go(0)
