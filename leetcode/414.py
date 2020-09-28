# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums: return 0
        
        first = second = third = float('-inf')
        
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            
            elif num > second and num < first:
                second, third = num, second
            
            elif num > third and num < second:
                third = num
        
        return third if third != float('-inf') else first