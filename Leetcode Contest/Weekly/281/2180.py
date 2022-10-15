# 2180. Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        
        for x in range(2, num + 1):
            s = sum(int(c) for c in str(x))
            if s % 2 == 0:
                res += 1
        
        return res
