# 1010. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        s = res = 0
        mp = Counter()
        
        for x in time:
            target = (60 - x) % 60
            
            res += mp[target]
            
            mp[x % 60] += 1
        
        return res
