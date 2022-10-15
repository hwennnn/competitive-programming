# 1094. Car Pooling
# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:(x[1], x[2], x[0]))
​
        dest = []
        
        for num, start, end in trips:
            capacity -= num
            
            while dest and dest[0][0] <= start:
                item = heapq.heappop(dest)
                capacity += item[1]
                
            if capacity < 0: return False
            heapq.heappush(dest, (end, num))
        
        return capacity >= 0
