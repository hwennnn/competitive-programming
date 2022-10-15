# 2259. Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        
        for i, x in enumerate(number):
            if x == digit:
                res = max(res, number[:i] + number[i + 1:])
        
        return res
