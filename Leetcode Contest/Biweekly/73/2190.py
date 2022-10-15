# 2190. Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        maxCount = res = 0
        
        for i in range(n - 1):
            if nums[i] == key:
                count = 0
                target = nums[i + 1]
                for j in range(i + 2, n):
                    if nums[j] == target:
                        count += 1
                
                if maxCount == 0 or count > maxCount:
                    res = target
                    maxCount = count
        
        return res
