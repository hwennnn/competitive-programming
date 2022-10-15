# 1864. Minimum Number of Swaps to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution:
    def minSwaps(self, s: str) -> int:
        counter = collections.Counter(s)
        if abs(counter['1'] - counter['0']) > 1: return -1
        
        n = len(s)
        
        def build(s):
            while len(s) < n:
                if s[-1] == "0":
                    s += "1"
                else:
                    s += "0"
            
            return s
        
        res1, res2 = build("0"), build("1")
​
        res = float('inf')
        
        def diff(A):
            return sum(a != b for a,b in zip(s, A))
        
        diff1, diff2 = diff(res1), diff(res2)
​
        if diff1 % 2 == 0:
            res = min(res, diff1)
        if diff2 % 2 == 0:
            res = min(res, diff2)
​
        return res // 2
        
        
        
        
