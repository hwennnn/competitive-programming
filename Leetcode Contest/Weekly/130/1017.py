# 1017. Convert to Base -2
# https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        res = []
​
        while n != 0:
            res.append(n & 1)
            n = -(n >> 1)
        
        return "".join(map(str, res[::-1] or [0]))
