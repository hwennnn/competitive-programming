# 1437. Check If All 1's Are at Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int):
        stack = []
        
        for i,x in enumerate(nums):
            if x == 1:
                if stack and i - stack[-1] <= k:
                    return False
                
                stack.append(i)
        
        return True