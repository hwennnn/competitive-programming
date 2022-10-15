# 1696. Jump Game VI
# https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = 0
        deq = collections.deque()
        
        for i in range(n-1,-1,-1):
            curr = nums[i] + (nums[deq[0]] if deq else 0)
            
            while (deq and curr > nums[deq[-1]]):
                deq.pop()
            
            deq.append(i)
            
            if deq[0] >= (i + k):
                deq.popleft()
            
            nums[i] = curr
        
        return curr