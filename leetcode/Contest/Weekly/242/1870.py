# 1870. Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        ihour = hour // 1 + (1 if hour % 1 != 0 else 0)
        if ihour < n: return -1
        
        def good(x):
            t = 0
            
            for i, d in enumerate(dist):
                if i != n - 1:
                    h = d // x + (1 if d % x != 0 else 0)
                else:
                    h = d / x
​
                t += h
​
            return t <= hour
            
​
        left, right = 1, 10 ** 7
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            
        
