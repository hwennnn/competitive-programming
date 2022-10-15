# 1705. Maximum Number of Eaten Apples
# https://leetcode.com/problems/maximum-number-of-eaten-apples/

from heapq import heappop, heappush

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        i = res = 0
        
        while True:
            if i < n:
                heappush(heap, (i+days[i], apples[i]))
            
            while heap and heap[0][0] <= i:
                heappop(heap)
                
            if heap:
                rot, apple = heappop(heap)
                res += 1
                
                if apple > 1:
                    heappush(heap, (rot, apple-1))
            
            if not heap and i >= n: break
            
            i += 1
        
        return res