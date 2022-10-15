# 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = total = 0
        
        for a,t in customers:
            current = max(current,a)
            
            total += current + t - a
            current += t
        
        return total / len(customers)