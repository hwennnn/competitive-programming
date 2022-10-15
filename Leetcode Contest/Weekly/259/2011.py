# 2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        
        for o in operations:
            if o == 'X++' or o == '++X':
                res += 1
            else:
                res -= 1
        
        return res
