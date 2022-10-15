# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        digits.sort()
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
