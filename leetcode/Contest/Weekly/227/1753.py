# 1753. Maximum Score From Removing Stones
# https://leetcode.com/problems/maximum-score-from-removing-stones

from heapq import heappush, heappop, heapify
​
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0
        stones = [-a,-b,-c]
        heapify(stones)
        
        while abs(stones[0]) > 0 and abs(stones[1]) > 0:
            first = heappop(stones) + 1
            second = heappop(stones) + 1
            
            heappush(stones, first)
            heappush(stones, second)
            
            res += 1
            
        return res
            
            
