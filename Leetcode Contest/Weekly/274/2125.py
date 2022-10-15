# 2125. Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = len(bank)
        prev = bank[0].count("1")
        res = 0
        
        for i in range(1, rows):
            curr = bank[i].count("1")
            
            if curr == 0: continue
                
            res += prev * curr
            
            prev = curr
        
        return res
