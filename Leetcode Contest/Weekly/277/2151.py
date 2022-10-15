# 2151. Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        
        res = 0
        
        for mask in range(1, 1 << n):
            valid = True
            good = 0
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    good += 1
                    for k in range(n):
                        if statements[j][k] == 2: continue
                        
                        if statements[j][k] == 0 and mask & (1 << k) > 0:
                            valid = False
                            break
                            
                        elif statements[j][k] == 1 and mask & (1 << k) == 0:
                            valid = False
                            break
            
            if valid:
                res = max(res, good)
        
        return res
