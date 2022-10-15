# 1702. Maximum Binary String After Change
# https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if "0" not in binary: return binary
        
        n = len(binary)
        first = binary.index('0')
        
        res = []
        for _ in range(first):
            res.append("1")
        
        zeroes = ones = 0
        for i in range(first, n):
            if binary[i] == "0":
                zeroes += 1
            else:
                ones += 1
        
        while zeroes > 1:
            res.append("1")
            zeroes -= 1
        
        res.append("0")
        
        while ones > 0:
            res.append("1")
            ones -= 1
        
        return "".join(res)
        