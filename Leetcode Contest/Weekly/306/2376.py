# 2376. Count Special Integers
# https://leetcode.com/problems/count-special-integers/

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        
        def f(n: int) -> int:
            digits = []
​
            while n > 0:
                digits.append(n % 10)
                n //= 10
​
            digits.reverse()
​
            N = len(digits)
​
            @cache
            def dp(pos, tight, start, rep, mask):
                if pos == N:
                    return 1 if rep else 0
​
                limit = digits[pos]
                if tight:
                    limit = 9
​
                res = 0
​
                for k in range(0, limit + 1):
                    nextStart = start | (k > 0)
                    nextTight = tight | (k < limit)
​
                    if nextStart:
                        res += dp(pos + 1, nextTight, nextStart, rep | (mask & (1 << k)) > 0, mask | (1 << k))
                    else:
                        res += dp(pos + 1, nextTight, 0, rep, mask)
​
                return res
​
            return dp(0, False, False, False, 0)
        
        return n - f(n)
