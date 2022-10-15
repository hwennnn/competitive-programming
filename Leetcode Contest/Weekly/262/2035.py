# 2035. Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        def construct(A):
            mp = {}
            N = len(A)
            
            for k in range(1, N + 1):
                sums = []
                for comb in combinations(A, k):
                    s = sum(comb)
                    sums.append(s)
                
                mp[k] = sums
            
            return mp
        
        leftPart, rightPart = nums[:n], nums[n:]
        leftSums, rightSums = construct(leftPart), construct(rightPart)
        res = abs(sum(leftPart) - sum(rightPart))
        total = sum(nums)
        half = total // 2
        
        for k in range(1, n):
            left, right = leftSums[k], rightSums[n - k]
            right.sort()
            
            for x in left:
                target = half - x
                index = bisect.bisect_left(right, target)
                
                for p in (index, index - 1):
                    if 0 <= p < len(right):
                        l = x + right[p]
                        r = total - l
                        res = min(res, abs(l - r))
        
        return res
        
