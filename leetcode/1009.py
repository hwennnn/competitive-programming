# 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        X = 1
        while N > X:
            X = X*2 + 1

        return X - N