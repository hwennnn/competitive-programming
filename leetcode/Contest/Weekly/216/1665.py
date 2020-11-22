# 1665. Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])

        ans = cur = 0
        for cost, mmin in tasks:
            if mmin > cur:
                ans += (mmin - cur)
                cur = mmin
            cur -= cost

        return ans