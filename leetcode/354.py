# 354. Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes

class Solution:
    def maxEnvelopes(self, en: List[List[int]]) -> int:
        en.sort(key = lambda x: (x[0], -x[1]))
        
        nums = [j for _, j in en]
        
        def lengthOfLIS(nums):
            stack = []
            for x in nums:
                index = bisect_left(stack, x)
                if index == len(stack):
                    stack.append(x)
                else:
                    stack[index] = x
​
            return len(stack)
        
        return lengthOfLIS(nums)
