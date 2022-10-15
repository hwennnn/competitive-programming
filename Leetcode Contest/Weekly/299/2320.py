# 2320. Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution:
    def countHousePlacements(self, n: int) -> int:
        M = 10 ** 9 + 7
        res = 0
        
        @cache
        def go(k):
            if k == 0: return 1
            if k == 1: return 2
​
            return go(k - 1) + go(k - 2)
        
        return (go(n) ** 2) % M
