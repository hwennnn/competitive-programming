# 2269. Find the K-Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, nums: int, k: int) -> int:
        num = str(nums)
        n = len(num)
        res = 0
        
        for i in range(n - k + 1):
            x = int(num[i : i + k])
​
            if x != 0 and nums % x == 0:
                res += 1
    
        return res
