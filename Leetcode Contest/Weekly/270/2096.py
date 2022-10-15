# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        mp = collections.defaultdict(tuple)
        res = []
        
        def go(node, parent):
            if not node: return
            
            mp[node.val] = (parent, node)
            go(node.left, node.val)
            go(node.right, node.val)
        
        go(root, -1)
        
        queue = deque([(startValue, "")])
        visited = set([startValue])
        
        while queue:
            x, path = queue.pop()
            
            if x == destValue:
                return path
            
            parent, node = mp[x]
            
            if parent not in visited:
                visited.add(parent)
                queue.append((parent, path + "U"))
            
            if node.left and node.left.val not in visited:
                visited.add(node.left.val)
                queue.append((node.left.val, path + "L"))
            
            if node.right and node.right.val not in visited:
                visited.add(node.right.val)
                queue.append((node.right.val, path + "R"))
​
