# 2099. Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = set(list(range(k)))
        heap = [(x, i) for i, x in enumerate(nums[:k])]
        heapq.heapify(heap) 
​
        for i, x in enumerate(nums[k:], k):
            res.add(i)
            value, index = heapq.heappushpop(heap, (x, i))
            res.remove(index)
            
        
        return [nums[i] for i in sorted(list(res))]
