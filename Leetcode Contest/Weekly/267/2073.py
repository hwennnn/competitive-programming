# 2073. Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] == 0: return 0
        
        A = deque([(index, t) for index, t in enumerate(tickets) if t > 0])
        time = 0
        
        while A:
            n = len(A)
            
            for _ in range(n):
                index, t = A.popleft()
                time += 1
                
                if index == k and t == 1:
                    return time
                
                if t - 1 > 0:
                    A.append((index, t - 1))
                
        
        
