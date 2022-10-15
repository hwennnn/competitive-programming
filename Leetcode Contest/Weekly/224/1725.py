# 1725. Number Of Rectangles That Can Form The Largest Square
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]):
        
        mp = collections.defaultdict(int)
        for a,b in rectangles:
            mp[min(a,b)] += 1

        return mp[max(mp)]
        