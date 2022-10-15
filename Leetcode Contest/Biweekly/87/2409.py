# 2409. Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(self, a: str, b: str, c: str, d: str) -> int:
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = [[0] * (month + 1) for month in months]
        
        def go(A, B):
            a, b = map(int, A.split('-'))
            c, d = map(int, B.split('-'))
            
            if a != c:
                for month in range(a, c):
                    if month == a:
                        for day in range(b, months[month] + 1):
                            days[month][day] += 1
                    else:
                        for day in range(months[month] + 1):
                            days[month][day] += 1
                            
                for day in range(1, d + 1):
                    days[c][day] += 1
                    
                return
            
            for day in range(b, d + 1):
                days[c][day] += 1
            
        res = 0
        go(a, b)
        go(c, d)
​
        for month in range(len(months)):
            for day in range(months[month] + 1):
                if day == 0: continue
                    
                if days[month][day] == 2:
                    res += 1
        
        return res
