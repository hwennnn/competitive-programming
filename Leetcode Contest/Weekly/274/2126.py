# 2126. Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for x in asteroids:
            if mass >= x:
                mass += x
            else:
                return False
        
        return True
