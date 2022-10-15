# 1980. Find Unique Binary String
# https://leetcode.com/problems/find-unique-binary-string/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set(nums)
        
        for i in range(1 << n):
            x = bin(i)[2:].zfill(n)
            if x not in s:
                return x
