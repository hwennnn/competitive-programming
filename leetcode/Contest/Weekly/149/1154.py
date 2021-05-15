# 1154. Day of the Year
# https://leetcode.com/problems/day-of-the-year/

from datetime import datetime
​
class Solution:
    def dayOfYear(self, date: str) -> int:
        f = "%Y-%m-%d"
        dt = datetime.strptime(date, f)
        res = dt.timetuple().tm_yday        
        
        return res
