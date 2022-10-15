# 2008. Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution:
    def maxTaxiEarnings(self, N: int, rides: List[List[int]]) -> int:
        
        n = len(rides)
        res = 0
        for ride in rides:
            ride[2] = ride[1] - ride[0] + ride[2]
        
        rides.sort(key = lambda x:(x[1]))
        dp = [[0, 0]]
        
        for start, end, profit in rides:
            index = bisect.bisect(dp, [start + 1]) - 1
            
            if dp[index][1] + profit > dp[-1][1]:
                dp.append([end, dp[index][1] + profit])
​
        return dp[-1][1]
