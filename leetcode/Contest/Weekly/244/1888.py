# 1888. Minimum Number of Flips to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        
        A, B = '', ''
        for i in range(len(s)):
            A += '1' if i % 2 == 0 else '0'
            B += '0' if i % 2 == 0 else '1'
        
        count1 = count2 = 0
        res = float('inf')
        for i in range(len(s)):
            if A[i] != s[i]: count1 += 1
            if B[i] != s[i]: count2 += 1
                
            if i >= n:
                if A[i - n] != s[i - n]: count1 -= 1
                if B[i - n] != s[i - n]: count2 -= 1
            
            if i >= (n - 1):
                res = min(res, count1, count2)
            
        return res
