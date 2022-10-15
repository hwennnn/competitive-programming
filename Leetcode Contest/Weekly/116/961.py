# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 2
        
        count = Counter(nums)
        
        for k, v in count.items():
            if v == n:
                return k
