# 1864. Minimum Number of Swaps to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating

class Solution:
    def minSwaps(self, s: str) -> int:
        ones = zeroes = 0
        
        for c in s:
            if c == '0': 
                zeroes += 1
            else:
                ones += 1
        
        if abs(ones - zeroes) > 1: return -1
        
        def countSwap(char):
            count = 0
            
            for c in s:
                if c != char:
                    count += 1
                
                char = "1" if char == "0" else "0"
            
            return count // 2
        
        if ones > zeroes: 
            return countSwap("1")
        elif zeroes > ones: 
            return countSwap("0")
        else:
            return min(countSwap("1"), countSwap("0"))
        
        
        
        
