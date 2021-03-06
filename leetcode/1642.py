# 1642. Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n - 1):
            delta = heights[i + 1] - heights[i]
            if delta > 0:
                heapq.heappush(heap, delta)
                if ladders > 0:
                    ladders -= 1
                else:
                    use = heapq.heappop(heap)
                    if bricks >= use:
                        bricks -= use
                    else:
                        return i
        
        return n - 1
