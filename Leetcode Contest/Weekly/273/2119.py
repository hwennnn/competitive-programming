# 2119. A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0
