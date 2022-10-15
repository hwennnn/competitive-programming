# 1742. Maximum Number of Balls in a Box
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mp = collections.defaultdict(int)
        
        for i in range(lowLimit, highLimit+1):
            value = 0
            
            while i >= 1:
                value += i%10
                i //= 10
                
            mp[value] += 1
​
        return max(mp.values())
