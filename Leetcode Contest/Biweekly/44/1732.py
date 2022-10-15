# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]):
        res = [0]
        for g in gain:
            res.append(res[-1] + g)
        
        return max(res)
        