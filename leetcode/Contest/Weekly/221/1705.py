# 1705. Maximum Number of Eaten Apples
# https://leetcode.com/problems/maximum-number-of-eaten-apples/

from heapq import heappop, heappush

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        res = i = 0
        q = []
        
        while True:
            if i < n:
                heappush(q, (i + days[i], apples[i]))
            
            while q and q[0][0] <= i:
                heappop(q)
            
            if q:
                d,a = heappop(q)
                res += 1
                
                if a > 1:
                    heappush(q, (d, a-1))
                
            
            if not q and i >= n: break
            
            i += 1
        
        return res