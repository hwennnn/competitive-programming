# 1185. Day of the Week
# https://leetcode.com/problems/day-of-the-week/

class Solution:
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]
        
