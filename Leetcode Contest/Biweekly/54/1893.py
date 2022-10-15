# 1893. Check if All the Integers in a Range Are Covered
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        A = [0] * 52
        
        for start,end in ranges:
            A[start] += 1
            A[end + 1] -= 1
        
        for i in range(1, 52):
            A[i] += A[i - 1]
​
        for i in range(left, right + 1):
            if A[i] <= 0: return False
        
        return True
