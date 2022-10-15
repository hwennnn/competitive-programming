# 2413. Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for x in range(1, n * 2 + 1):
            if x % 2 == 0 and x % n == 0:
                return x
        
        return -1
