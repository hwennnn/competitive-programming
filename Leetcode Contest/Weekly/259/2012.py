# 2012. Sum of Beauty in the Array
# https://leetcode.com/problems/sum-of-beauty-in-the-array/

from sortedcontainers import SortedList
​
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left = SortedList()
        left.add(nums[0])
        
        right = SortedList()
        for i in range(2, n):
            right.add(nums[i])
        res = 0
        
        for i in range(1, n - 1):
            left_index = left.bisect(nums[i])
            right_index = right.bisect_left(nums[i])
​
            if left_index == len(left) and left[left_index - 1] < nums[i] and right_index == 0 and right[0] > nums[i]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
                
            left.add(nums[i])
            right.remove(nums[i + 1])
​
        return res
