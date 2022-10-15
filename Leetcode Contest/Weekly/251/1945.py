# 1945. Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''
        
        for c in s:
            ss += str(ord(c) - ord('a') + 1)
​
        for _ in range(k):
            ss = str(sum(int(i) for i in ss))
            
        return int(ss)
