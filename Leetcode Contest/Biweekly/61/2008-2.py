# 2008. Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        A = []
        
        for index, (start, end, profit) in enumerate(rides):
            A.append((start, 1, index))
        
        heapq.heapify(A)
        curr_best = 0
        
        while len(A) > 0:
            current, t, x = heapq.heappop(A)
            
            if t == 1:
                end = rides[x][1]
                heapq.heappush(A, (end, -1, curr_best + end - current + rides[x][2]))
            else:
                curr_best = max(curr_best, x)
        
        return curr_best
        
