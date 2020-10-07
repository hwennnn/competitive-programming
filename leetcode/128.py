# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for x in nums:
            if x - 1 not in s:
                y = x + 1
                
                if y in s:
                    while y in s:
                        y += 1

                res = max(res, y - x)
        
        return res


# Another approach: remove element once found
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        while s:
            first = last = s.pop()
            
            while first - 1 in s:
                first -= 1
                s.remove(first)
            
            while last + 1 in s:
                last += 1
                s.remove(last)
            
            res = max(res, last - first + 1)
        
        return res