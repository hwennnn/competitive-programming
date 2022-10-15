# 1006. Clumsy Factorial
# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        
        while n > 0:
            stack.append(stack.pop() * n)
            n -= 1
            
            if n > 0:
                stack.append(stack.pop() // n)
                n -= 1
            
            if n > 0:
                stack.append(n)
                n -= 1
            
            if n > 0:
                stack.append(-1 * n)
                n -= 1
        
        return sum(stack)
