# 89. Gray Code
# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int):
        return [i ^ i >> 1 for i in range(1 << n)]

    def grayCode(self, n: int):
        res = [0]
        
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j] | 1 << i)
        
        return res