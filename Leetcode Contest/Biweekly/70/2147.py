# 2147. Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        M = 10 ** 9 + 7
        seats = corridor.count("S")
        if seats % 2 == 1 or seats < 2: return 0
        
        s = [i for i, x in enumerate(corridor) if x == "S"]
        res = 1
        
        for i in range(1, len(s) - 1, 2):
            res *= (s[i + 1] - s[i])
        
        return res % M
            
