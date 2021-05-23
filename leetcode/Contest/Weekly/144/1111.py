# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution:
    def maxDepthAfterSplit(self, seq):
        A = B = 0
        res = [0] * len(seq)
        
        for i, c in enumerate(seq):
            v = 1 if c == '(' else -1
            if (v > 0) == (A < B):
                A += v
            else:
                B += v
                res[i] = 1
                
        return res
