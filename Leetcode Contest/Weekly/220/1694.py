# 1694. Reformat Phone Number
# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        num = "".join(c for c in number if c.isdigit())
        
        i = 0
        n = len(num)
        res = ""
        
        while n > 4:
            res += num[i:i+3] + "-"
            i += 3
            n -= 3
                
        if n == 4:
            res += num[i:i+2] + "-" + num[i+2:i+4]

        else:
            res += num[i:i+n]

        return res