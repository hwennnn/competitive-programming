# 2042. Check if Numbers Are Ascending in a Sentence
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        nums = []
        
        for x in s:
            if x.isnumeric():
                nums.append(int(x))
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]: return False
        
        return True
