# 1814. Count Nice Pairs in an Array
# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = Counter(num - int(str(num)[::-1]) for num in nums)
        
        return sum((c * (c-1) // 2) for c in count.values()) % (10 ** 9 + 7)
