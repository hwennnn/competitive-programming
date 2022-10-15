# 1962. Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
​
        for _ in range(k):
            pile = -heapq.heappop(heap)
            heapq.heappush(heap, -ceil(pile / 2))
            
        return sum([-pile for pile in heap])
