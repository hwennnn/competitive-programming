# 2264. Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
​
        for key, group in itertools.groupby(num):
            if len(list(group)) >= 3:
                res = max(res, key * 3)
​
        return res
                
