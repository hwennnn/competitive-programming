# 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        full = (1 << n.bit_length()) - 1
        
        return full ^ n
