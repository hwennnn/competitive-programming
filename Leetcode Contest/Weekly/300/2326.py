# 2326. Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, rows: int, cols: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * cols for _ in range(rows)]
​
        rowStart, rowEnd = 0, rows - 1
        colStart, colEnd = 0, cols - 1
        
        while head:
            # traverse right
            i = colStart
            while head and i <= colEnd:
                matrix[rowStart][i] = head.val
                head = head.next
                i += 1
            rowStart += 1
            
            # traverse down
            i = rowStart
            while head and i <= rowEnd:
                matrix[i][colEnd] = head.val
                head = head.next
                i += 1
            colEnd -= 1
            
            # traverse left
            i = colEnd
            while head and i >= colStart:
                matrix[rowEnd][i] = head.val
                head = head.next
                i -= 1
            rowEnd -= 1
        
            # traverse up
            i = rowEnd
            while head and i >= rowStart:
                matrix[i][colStart] = head.val
                head = head.next
                i -= 1
            colStart += 1   
        
        return matrix
