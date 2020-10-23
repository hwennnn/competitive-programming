# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/

class Solution:
    # O(N)
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s3 = [], float('-inf')
        
        for i in nums[::-1]:
            if i < s3: return True
            else:
                while stack and i > stack[-1]:
                    s3 = stack.pop()
            
            stack.append(i)
        
        return False

    def find132pattern(self, nums: List[int]) -> bool:
        i = float('inf')
    
        for j in range(len(nums)):
            i = min(i, nums[j])
            if i == nums[j]: continue
                
            for k in range(j+1, len(nums)):
                if i < nums[k] and nums[k] < nums[j]:
                    return True
        
        return False
