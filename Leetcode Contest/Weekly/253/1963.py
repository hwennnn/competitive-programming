# 1963. Minimum Number of Swaps to Make the String Balanced
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        count = res = 0
        
        for c in s:
            if c == '[':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                res += 1
                count = 1
        
        return res
