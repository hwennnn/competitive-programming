# 2310. Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        
        for i in range(1, 11):
            if (i * k) % 10 == num % 10 and i * k <= num:
                return i
        
        return -1