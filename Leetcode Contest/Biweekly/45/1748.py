# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        return sum(n for n in cnt if cnt[n] == 1)
