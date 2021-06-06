# 1887. Reduction Operations to Make the Array Elements Equal
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        keys = sorted(counter.keys(), reverse = 1)
        curr = res = 0
        
        for key in keys[:-1]:
            curr += counter[key]
            res += curr
        
        return res
        
