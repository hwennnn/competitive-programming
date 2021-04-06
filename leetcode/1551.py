# 1551. Minimum Operations to Make Array Equal
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i) + 1 for i in range(n)]
        t = sum(arr) // n
        
        res = 0
        
        for num in arr:
            res += abs(t - num)
        
        return res // 2
