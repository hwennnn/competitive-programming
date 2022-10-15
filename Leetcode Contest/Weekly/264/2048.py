# 2048. Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        c = Counter(str(n))
        
        def good(c):
            for k, v in c.items():
                if int(k) != v:
                    return False
            
            return True
        
        while not good(c):
            n += 1
            c = Counter(str(n))
        
        return n
