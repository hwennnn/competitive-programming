# 2001. Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mp = collections.defaultdict(int)
        res = 0
        
        for x, y in rectangles:
            if x / y in mp:
                res += mp[x / y]
                
            mp[x / y] += 1
        
        return res
