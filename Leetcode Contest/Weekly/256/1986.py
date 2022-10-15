# 1986. Minimum Number of Work Sessions to Finish the Tasks
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        
        @cache
        def go(mask, curr, session):
            if mask == 0: return session
            
            res = float('inf')
            
            for i in range(n):
                if mask & (1 << i):
                    if curr + tasks[i] <= sessionTime:
                        res = min(res, go(mask ^ (1 << i), curr + tasks[i], session))
                    else:
                        res = min(res, go(mask ^ (1 << i), tasks[i], session + 1))
            
            return res
        
        return go((1 << n) - 1, 0, 1)
