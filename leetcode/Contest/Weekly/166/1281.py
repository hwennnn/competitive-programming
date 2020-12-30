# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        c = 0
        
        for i,x in enumerate(str(n)):
            p *= int(x)
            c += int(x)
        
        return p - c