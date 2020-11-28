# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deq = collections.deque()
        res = []
        
        for i, x in enumerate(nums):
            if i >= k:
                if deq[0] == nums[i-k]:
                    deq.popleft()
            
            while deq and deq[-1] < x:
                deq.pop()
            
            deq.append(x)
            
            if i >= k-1:
                res.append(deq[0])
        
        return res
