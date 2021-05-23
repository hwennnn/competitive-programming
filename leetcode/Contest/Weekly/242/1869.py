# 1869. Longer Contiguous Segments of Ones than Zeros
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = zeroes = 0
        
        for k, g in itertools.groupby(s):
            if k == "1":
                ones = max(ones, len(list(g)))
            else:
                zeroes = max(zeroes, len(list(g)))
​
        return ones > zeroes
