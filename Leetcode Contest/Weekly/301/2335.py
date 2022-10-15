# 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        H = [-x for x in amount if x != 0]
        heapify(H)
        
        while H:
            if len(H) >= 2:
                first, second = heappop(H), heappop(H)
                first = -first
                second = -second
                
                first -= 1
                second -= 1
                if first > 0:
                    heappush(H, -first)
                if second > 0:
                    heappush(H, -second)
                res += 1
            else:
                res += -heappop(H)
        
        return res
