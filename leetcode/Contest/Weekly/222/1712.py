# 1712. Ways to Split Array Into Three Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution:
    def waysToSplit(self, nums: List[int]):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        M = 10 ** 9 + 7
        ans = 0
        for i in range(1, len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            ans += max(0, min(len(nums), k) - max(i+1, j))

        return ans % M
    
    def helper(self, prefix, leftSum, i, searchLeft):
        n = len(prefix)
        left, right = i, n - 2
        res = -1
        
        while left <= right:
            mid = left + (right-left) // 2
            
            midSum = prefix[mid] - prefix[i - 1]
            rightSum = prefix[-1] - prefix[mid]
            
            if leftSum <= midSum <= rightSum:
                res = mid
                if searchLeft: right = mid - 1
                else: left = mid + 1
            elif leftSum > midSum:
                left = mid + 1
            else:
                right = mid - 1
        
        return res
        
    def waysToSplit(self, nums: List[int]):
        
        M = 10 ** 9 + 7
        n = len(nums)
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
        
        res = 0
        for i in range(1, n-1):
            leftSum = prefix[i-1]
            
            mid = self.helper(prefix, leftSum, i, True)
            right = self.helper(prefix, leftSum, i, False)
            
            if mid == -1 or right == - 1: continue
            
            res += (right - mid + 1) 
            res %= M
        
        return res % M
    