# 2283. Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        
        for i, x in enumerate(num):
            if count[str(i)] != int(x):
                return False
        
        return True
