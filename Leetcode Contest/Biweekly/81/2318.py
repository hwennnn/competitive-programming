# 2318. Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/

class Solution:
    def distinctSequences(self, n: int) -> int:
        M = 10 ** 9 + 7
        res = 0
        g = [[False] * 7 for _ in range(7)]
​
        for i in range(1, 7):
            for j in range(1, 7):
                if gcd(i, j) == 1:
                    g[i][j] = True
        
        @cache
        def go(index, prev1, prev2):
            if index == n: return 1
            
            res = 0
            for dice in range(1, 7):
                if dice != prev1 and dice != prev2 and (prev1 == 0 or g[dice][prev1]):
                    res += go(index + 1, dice, prev1)
                    res %= M
            
            return res % M
                        
        return go(0, 0, 0)
