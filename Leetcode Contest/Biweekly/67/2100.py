# 2100. Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0: return list(range(n))
        if n <= time * 2: return []
        
        res = []
        inc = [1] * n
        dec = [1] * n
        
        curr = 1
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                curr += 1
            else:
                curr = 1
            
            inc[i] = curr
        
        curr = 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                curr += 1
            else:
                curr = 1
            
            dec[i] = curr
                    
        for i in range(n):
            if inc[i] - 1 >= time and dec[i] - 1 >= time:
                res.append(i)
            
        return res
            
