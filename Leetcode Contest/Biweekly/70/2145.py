# 2145. Count the Hidden Sequences
# https://leetcode.com/problems/count-the-hidden-sequences/

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mmax = mmin = s = 0
        
        for x in differences:
            s += x
            
            mmax = max(mmax, s)
            mmin = min(mmin, s)
        
        return max(0, (upper - lower) - (mmax - mmin) + 1)
