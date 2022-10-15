# 1964. Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        sl = []
        res = []
        
        for obs in obstacles:
            if len(sl) == 0 or sl[-1] <= obs:
                sl.append(obs)
                res.append(len(sl))
            else:
                index = bisect.bisect(sl, obs)
                sl[index] = obs
​
                res.append(index + 1)
​
        return res
