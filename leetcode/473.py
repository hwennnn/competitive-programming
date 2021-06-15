# 473. Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        n = len(sticks)
        ssum = sum(sticks)
        target = ssum // 4
        if ssum % 4 != 0: return False
        dp = {}
        
        sticks.sort(reverse = 1)
        
        def hashing(curr, formed, used):
            return (curr, formed, tuple(list(sorted(used))))
        
        def go(curr, formed, used):
            hashed = hashing(curr, formed, used)
            if hashed in dp: return dp[hashed]
                      
            if formed == 4 and len(used) == n: return True
            
            for i in range(n):
                if i in used: continue
                
                if curr + sticks[i] == target:
                    used.add(i)
                    result = go(0, formed + 1, used)
                    if result: return True
                    dp[hashing(0, formed + 1, used)] = result
                    used.remove(i)  
                elif curr + sticks[i] < target:
                    used.add(i)
                    result = go(curr + sticks[i], formed, used)
                    if result: return True
                    dp[hashing(curr + sticks[i], formed, used)] = result
                    used.remove(i)
            
            return False
        
        return go(0, 0, set())
