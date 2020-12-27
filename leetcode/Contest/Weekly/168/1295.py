# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        
        for num in map(str,nums):
            res += (len(num) % 2 == 0)
        
        return res