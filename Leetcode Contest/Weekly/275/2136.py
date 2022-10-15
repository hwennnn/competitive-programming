# 2136. Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = [(x, y) for x, y in zip(plantTime, growTime)]
        A.sort(key = lambda x:-x[1])
        
        days = 0
        res = 0
        
        for plant, grow in A:
            days += plant
            
            res = max(res, days + grow)
        
        return res
