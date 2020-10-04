# 1609. Even Odd Tree
# https://leetcode.com/problems/even-odd-tree/

from collections import deque  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printLevelOrder(self, root): 

        if root is None: 
            return
        
        q = [] 
        q.append(root) 
        i = 0
        isEven = True
        while q: 

            prev = None
            count = len(q)
            
            while count > 0: 
                temp = q.pop(0) 
                num = temp.val
                if temp.left: 
                    q.append(temp.left) 
                if temp.right: 
                    q.append(temp.right) 
                    
                if isEven:
                    if num%2 == 0 or prev and num <= prev:
                        return False
                else:
                    if num%2 or prev and num >= prev:
                        return False

                prev = num
                count -= 1
            isEven = not isEven
                
        return True
    
    def isEvenOddTree(self, root: TreeNode) -> bool:
        return self.printLevelOrder(root)  
        