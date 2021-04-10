# 1780. Check if Number is a Sum of Powers of Three
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 2: return False
            
            n //= 3
            
        return n == 1
