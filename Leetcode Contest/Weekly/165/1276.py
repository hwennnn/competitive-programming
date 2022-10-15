# 1276. Number of Burgers with No Waste of Ingredients
# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        
        a = (t-2*c) / 2
        b = c - a
        
        return [int(a),int(b)] if int(a) == a and int(b) == b and a >= 0 and b >= 0 else []