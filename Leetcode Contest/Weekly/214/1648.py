# 1648. Sell Diminishing-Valued Colored Balls
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

from heapq import heappop, heappush

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        M = 1000000007
        
        pq = []
        for v in inventory:
            heappush(pq, (-v, 1))

        res = 0
        
        while pq and orders > 0:
            top, count = pq[0]
            top = -top
            heappop(pq)
            
            while pq and pq[0][0] == -top:
                count += pq[0][1]
                heappop(pq)
            
            next_top = 0
            if pq:
                next_top = -pq[0][0]
                
            delta = top - next_top
            
            if delta * count <= orders:
                d = (top*(top+1)) //2
                d -= (next_top*(next_top+1)) // 2
                d *= count
                orders -= delta * count
                res += d
                res %= M
            else:
                num = orders // count
                d = (top*(top+1)) //2
                next_top = top - num
                d -= (next_top*(next_top+1)) // 2
                d *= count
                
                res += d
                orders -= num * count
                
                leftover = orders % count
                res += next_top * leftover
                res %= M
                orders -= leftover
                
            if next_top:
                heappush(pq, (-next_top, count))

        
        return res % M