# 2327. Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M = 10 ** 9 + 7
        res = 1
​
        canShare = defaultdict(int)
​
        toForget = defaultdict(int)
        toForget[forget + 1] = 1
​
        propagate = 1
        
        for day in range(delay + 1, n + 1):
            propagate += canShare[day]    
            propagate -= toForget[day]
            
            res += propagate
            res -= toForget[day]
            res %= M
​
            canShare[day + delay] += propagate
            toForget[day + forget] += propagate
​
        
        return res % M
